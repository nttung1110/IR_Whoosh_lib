from os import path
from whoosh.index import create_in
from whoosh.fields import *
from tqdm import tqdm
from whoosh.qparser import QueryParser
from whoosh import qparser

import pdb
import json

def construct_idx(path_document):
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    ix = create_in("indexdir", schema)
    writer = ix.writer()

    with open(path_document, "r") as fp:
        json_data = json.load(fp)['all_documents']


    gen_name_dir = 0
    for each_document in tqdm(json_data):
        title = each_document["ori_title"]
        content = each_document["ori_text"]

        writer.add_document(title=title, path="/"+str(gen_name_dir), content=content)
        gen_name_dir += 1
    writer.commit()

    return ix


def get_result(query_parser, searcher, query_input, limit_res):

    query = query_parser.parse(query_input)
    results = searcher.search(query, limit=limit_res)

    num_res = len(results)
    if num_res == 0:
        print("No similar documents found")
    else:
        print("Found documents")
    for i in range(len(results)):
        print(results[i])
        if i >= limit_res - 1:
            break


if __name__ == "__main__":
    path_document = '../TF-IDF-Document-Retrieval/standard_all_documents.json'

    # First perform indexing the document
    ix_builder = construct_idx(path_document)

    # Build searcher and query parser
    searcher = ix_builder.searcher()
    query_parser = QueryParser("content", ix_builder.schema, group=qparser.OrGroup)

    # specify user input
    query_input = "president christmas"
    limit_res = 50
    
    get_result(query_parser, searcher, query_input, limit_res)

