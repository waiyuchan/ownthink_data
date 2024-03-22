import csv
import pandas as pd
import redis
from sqlalchemy import create_engine, text

# 数据库配置
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Test123456',
    'db': 'knowledgegraph',
    'charset': 'utf8mb4'
}

# Redis配置
redis_config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

# 创建数据库连接
engine = create_engine(
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db']}?charset={db_config['charset']}")
r = redis.Redis(**redis_config)


def find_in_cache_or_db(conn, table, column, value):
    """
    优先从Redis缓存查询ID，如果没有则从数据库查询，并更新缓存。
    """
    cache_key = f"{table}:{column}:{value}"
    id = r.get(cache_key)
    if id:
        return int(id)
    else:
        result = conn.execute(text(f"SELECT id FROM {table} WHERE {column} = :value"), {'value': value})
        row = result.fetchone()
        if row:
            r.set(cache_key, row[0])
            return row[0]
    return None


def process_batch(conn, batch, missing_data_writer):
    """
    处理一批数据，返回要插入triple表的数据列表。
    """
    triples_list = []
    for _, row in batch.iterrows():
        entity_id = find_in_cache_or_db(conn, 'entity', 'entity', row['实体'])
        relation_id = find_in_cache_or_db(conn, 'relation', 'relation', row['属性'])
        if entity_id and relation_id:
            subject_id = find_in_cache_or_db(conn, 'entity', 'entity', row['值'])
            subject_type = 0 if subject_id else 1  # 默认为0，如果找不到则尝试property表
            if not subject_id:  # 如果在entity表中未找到，尝试property表
                subject_id = find_in_cache_or_db(conn, 'property', 'property', row['值'])
            if subject_id:
                triples_list.append((entity_id, relation_id, subject_id, subject_type))
            else:
                missing_data_writer.writerow([row['实体'], row['属性'], row['值']])
        else:
            missing_data_writer.writerow([row['实体'], row['属性'], row['值']])
    return triples_list


def batch_insert_triples(conn, triples_list):
    """
    批量插入三元组数据。
    """
    if triples_list:
        conn.execute(text(
            "INSERT INTO triple (object_id, relation, subject_id, subject_type) VALUES (:object_id, :relation, :subject_id, :subject_type)"),
            triples_list)


def main():
    # CSV文件路径
    csv_file = 'data/ownthink_v2.csv'
    missing_data_file = 'data/missing_data.csv'

    with engine.connect() as conn, open(missing_data_file, 'w', newline='', encoding='utf-8') as f:
        missing_data_writer = csv.writer(f)
        missing_data_writer.writerow(['实体', '属性', '值'])  # 写入头部

        # 分批读取并处理CSV文件
        for batch in pd.read_csv(csv_file, chunksize=1000):  # 每次处理1000行
            triples_list = process_batch(conn, batch, missing_data_writer)
            batch_insert_triples(conn, triples_list)
            print("Batch processed and inserted into database.")


if __name__ == "__main__":
    main()
