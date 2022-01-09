from os import path
from whoosh.index import create_in
from whoosh.fields import *
from tqdm import tqdm
from whoosh.qparser import QueryParser

import pdb
import json
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()

path_document = '../TF-IDF-Document-Retrieval/standard_all_documents.json'
with open(path_document, "r") as fp:
    json_data = json.load(fp)['all_documents']


gen_name_dir = 0
for each_document in tqdm(json_data):
    title = each_document["ori_title"]
    content = each_document["ori_text"]

    writer.add_document(title=title, path="/"+str(gen_name_dir), content=content)
    gen_name_dir += 1
writer.commit()

searcher = ix.searcher()
query = QueryParser("content", ix.schema).parse("listen fox news articles")
results = searcher.search(query)
pdb.set_trace()
for i in range(len(results)):
    print(results[i])
