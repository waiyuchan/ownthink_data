import pandas as pd

file_path = 'data/ownthink_v2.csv'
relation_output_file_path = 'data/relation.csv'
chunk_size = 100000
relation_list = []


def relation_processor(chunk):
    for index, row in chunk.iterrows():
        relation_list.append(row["属性"])


chunks = pd.read_csv(file_path, chunksize=chunk_size)

for chunk in chunks:
    relation_processor(chunk)

relation_set = set(relation_list)
unique_relations = list(relation_set)
df_unique_relations = pd.DataFrame(unique_relations, columns=['Relation'])
df_unique_relations.to_csv(relation_output_file_path, index=False)
