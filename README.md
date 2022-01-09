# Whoosh libracy custom usage

## Introduction

A simple demonstration of using Whoosh library for indexing documents

The retrieval pipeline is as following:

+ Crawl news data on the internet.
+ Preprocess data and construct Index with Whoosh library. 
+ Input query and preprocess query data.
+ Search and show the results.

## Environment Settings

Please follow my previous setups guide [TF-IDF-Document-Retrieval](https://github.com/nttung1110/TF-IDF-Document-Retrieval)

## Crawling the data and building documents

Please follow my previous implementation step by step to crawl and process the documents[TF-IDF-Document-Retrieval](https://github.com/nttung1110/TF-IDF-Document-Retrieval)

## Whoosh library for indexing documents

Now we have the documents being standardized. These documents were stored in json file which can be then used for indexing documents with the help of Whoosh library.

Change some parameters in `simeple_whoosh_demo.py` as following:

```
query_input = #YOUR QUERY
limit_res = #LIMITED NUMBER OF RESULTS
path_document = #PATH TO JSON DATA OF DOCUMENTS
```

Then run the script to perform the search.
