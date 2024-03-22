import pandas as pd

filepath = 'data/ownthink_v2.csv'
entity_output_filepath = 'data/entity.csv'
chunk_size = 50000
entity_list = []


def entity_processor(chunk):
    for index, row in chunk.iterrows():
        entity_list.append(row["实体"])


chunks = pd.read_csv(filepath, chunksize=chunk_size)

for chunk in chunks:
    entity_processor(chunk)

entity_set = set(entity_list)
unique_entities = list(entity_set)
df_unique_entities = pd.DataFrame(unique_entities, columns=['Entity'])
df_unique_entities.to_csv(entity_output_filepath, index=False)
