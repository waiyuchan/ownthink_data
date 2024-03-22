import pandas as pd

file_path = 'data/ownthink_v2.csv'
initial_property_output_filepath = 'data/tmp_property.csv'
entity_filepath = 'data/entity.csv'
processed_property_output_file_path = 'data/property.csv'
chunk_size = 100000
property_list = []


def property_processor(chunk):
    for index, row in chunk.iterrows():
        property_list.append(row["值"])


chunks = pd.read_csv(file_path, chunksize=chunk_size)

for chunk in chunks:
    property_processor(chunk)

property_set = set(property_list)
unique_properties = list(property_set)
df_unique_properties = pd.DataFrame(unique_properties, columns=['Property'])
df_unique_properties.to_csv(initial_property_output_filepath, index=False)

data_initial_property = pd.read_csv(initial_property_output_filepath, usecols=['Property'])
data_entity_df = pd.read_csv(entity_filepath, usecols=['Entity'])

# 转换成列表，以便使用isin方法
data_entity = data_entity_df['Entity'].tolist()

# 使用isin方法找到需要过滤掉的数据
mask = data_initial_property['Property'].isin(data_entity)

# 过滤掉这些数据
filtered_data_initial_property = data_initial_property[~mask]

# 文件保存
filtered_data_initial_property.to_csv(processed_property_output_file_path, index=False)
