import pandas as pd
import os


class Spliter:

    def split_csv(file_path, output_folder, split_size):
        """
        拆分CSV文件为多个小文件。

        :param file_path: 要拆分的CSV文件的路径。
        :param output_folder: 存储拆分后的文件的文件夹。
        :param split_size: 每个小文件的行数。
        """
        # 确保输出文件夹存在
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        df = pd.read_csv(file_path)  # 读取整个文件

        num_splits = len(df) // split_size + (1 if len(df) % split_size else 0)  # 计算需要拆分成多少个文件

        for i in range(num_splits):
            df_subset = df.iloc[i * split_size:(i + 1) * split_size]  # 分割DataFrame
            output_file = f"{output_folder}/{os.path.basename(output_folder)}_{str(i + 1).zfill(2)}.csv"  # 构造输出文件路径
            df_subset.to_csv(output_file, index=False)  # 保存到CSV

    def split_large_csv(file_path, output_folder, split_size):
        """
        分块读取和拆分大型CSV文件。

        :param file_path: 要拆分的CSV文件的路径。
        :param output_folder: 存储拆分后的文件的文件夹。
        :param split_size: 每个小文件的行数。
        """
        # 确保输出文件夹存在
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        chunk_counter = file_counter = 0  # 初始化计数器
        df_accumulator = pd.DataFrame()  # 初始化DataFrame存储器

        # 分块读取文件
        for chunk in pd.read_csv(file_path, chunksize=split_size):
            df_accumulator = pd.concat([df_accumulator, chunk], ignore_index=True)  # 将当前块的数据添加到累加器DataFrame中

            # 检查累加器中的行数是否达到了指定的split_size
            if len(df_accumulator) >= split_size:
                file_counter += 1
                output_file = f"{output_folder}/{os.path.basename(output_folder)}_{str(file_counter).zfill(2)}.csv"  # 构造输出文件路径
                df_accumulator[:split_size].to_csv(output_file, index=False)  # 保存累加器中的数据到CSV
                df_accumulator = df_accumulator[split_size:]  # 更新累加器，去除已经保存的数据

            chunk_counter += 1

        # 检查并保存剩余的数据（如果有的话）
        if not df_accumulator.empty:
            file_counter += 1
            output_file = f"{output_folder}/{os.path.basename(output_folder)}_{str(file_counter).zfill(2)}.csv"
            df_accumulator.to_csv(output_file, index=False)


if __name__ == '__main__':
    Spliter.split_csv("data/entity_export.csv", "data/entity_export", 10000)
    Spliter.split_csv("data/property_export.csv", "data/property_export", 10000)
    Spliter.split_csv("data/relation_export.csv", "data/relation_export", 10000)
    Spliter.split_large_csv("data/ownthink_v2.csv", "data/ownthink_v2", 100000)
