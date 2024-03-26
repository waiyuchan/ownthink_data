import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor


def process_file(input_file, entity_folder, property_folder, relation_folder, output_file):
    """
    处理单个文件，执行搜索并写入结果。

    :param input_file: 输入文件路径。
    :param entity_folder: 实体所在的文件夹路径。
    :param property_folder: 属性所在的文件夹路径。
    :param relation_folder: 关系所在的文件夹路径。
    :param output_file: 输出文件路径。
    """
    # 读取文件
    df = pd.read_csv(input_file)

    # 准备结果DataFrame
    result_df = pd.DataFrame(
        columns=['entity_id', 'entity', 'relation_id', 'relation', 'subject_id', 'subject', 'subject_type'])

    for index, row in df.iterrows():
        # 执行搜索
        entity_id = quick_search(row['实体'], entity_folder)
        relation_id = quick_search(row['属性'], relation_folder)
        subject_id = quick_search(row['值'], entity_folder)
        subject_type = 0  # 假设默认为0
        if subject_id is None:
            subject_id = quick_search(row['值'], property_folder)
            subject_type = 1

        # 更新结果DataFrame
        result_df = result_df.append({
            'entity_id': entity_id,
            'entity': row['实体'],
            'relation_id': relation_id,
            'relation': row['属性'],
            'subject_id': subject_id,
            'subject': row['值'],
            'subject_type': subject_type
        }, ignore_index=True)

    # 保存结果到CSV
    result_df.to_csv(output_file, index=False)


def process_all_files(input_folder, entity_folder, property_folder, relation_folder, output_folder):
    """
    并行处理所有文件。

    :param input_folder: 输入文件所在的文件夹。
    :param entity_folder: 实体所在的文件夹路径。
    :param property_folder: 属性所在的文件夹路径。
    :param relation_folder: 关系所在的文件夹路径。
    :param output_folder: 结果文件存储的文件夹。
    """
    files = os.listdir(input_folder)
    with ThreadPoolExecutor(max_workers=4) as executor:
        for file in files:
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, file.replace('.csv', '_result.csv'))
            executor.submit(process_file, input_file, entity_folder, property_folder, relation_folder, output_file)


# 调用函数处理所有文件
# 注意：确保entity_export, property_export, relation_export, 和 ownthink_v2文件夹已正确设置并包含了所需的CSV文件
process_all_files("ownthink_v2", "entity_export", "property_export", "relation_export", "ownthink_v2_results")
