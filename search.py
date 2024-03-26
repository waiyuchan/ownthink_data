import threading
import pandas as pd
import os
from queue import Queue
import time


def file_search(file_path, search_str, result_queue):
    """
    在一个CSV文件中搜索指定的字符串。

    :param file_path: CSV文件的路径。
    :param search_str: 要搜索的字符串。
    :param result_queue: 用于存储搜索结果的队列。
    """
    try:
        df = pd.read_csv(file_path)
        # 逐行检查是否有列包含search_str
        for index, row in df.iterrows():
            if search_str in row.to_string():
                # 如果找到匹配，将第一个匹配的id放入结果队列
                result_queue.put(row['id'])
                return
    except Exception as e:
        print(f"Error searching in file {file_path}: {e}")
        # 如果没有找到，或者有错误发生，什么都不做
    result_queue.put(None)


def quick_search(search_str, folder):
    """
    快速搜索指定文件夹内的所有CSV文件。

    :param search_str: 要搜索的字符串。
    :param folder: 包含CSV文件的文件夹路径。
    """
    # 创建一个队列来存储搜索结果
    result_queue = Queue()

    # 获取文件夹内所有文件的路径
    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    # 创建并启动搜索线程
    threads = []
    for file_path in files:
        t = threading.Thread(target=file_search, args=(file_path, search_str, result_queue))
        t.start()
        threads.append(t)

    # 等待所有线程完成
    for t in threads:
        t.join()

    # 检查队列中的所有结果，选择第一个非None的结果作为最终结果
    final_result = None
    while not result_queue.empty():
        result = result_queue.get()
        if result is not None:
            final_result = result
            break

    return final_result


if __name__ == '__main__':
    start_time = time.time()  # 获取开始时间
    result_id = quick_search("贵州大学土木工程学院", "data/entity_export")
    end_time = time.time()  # 获取结束时间
    elapsed_time = end_time - start_time  # 计算经过的时间
    print(f"找到的ID: {result_id}")
    print(f"搜索耗时: {elapsed_time} 秒")

    start_time = time.time()  # 获取开始时间
    result_id = quick_search(
        "\"小说类型散文诗词内容简介我是无神论者,这却是逼不得已,无可奈何的事儿,因为问题是,谁叫我到现在还未能亲眼看见鬼啊神啊的,能有什么亲身经历啊!倘若理由是我没有那么的一种“缘分”、“福分”,那就对不起了,我始终不能人云亦云,只因为不要怀疑只要信而轻易信服,心服口服得了的……...\"",
        "data/property_export")
    end_time = time.time()  # 获取结束时间
    elapsed_time = end_time - start_time  # 计算经过的时间
    print(f"找到的ID: {result_id}")
    print(f"搜索耗时: {elapsed_time} 秒")
