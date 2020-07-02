#!/usr/bin/env python
# -*- coding: utf-8 -*-

import leveldb
import gzip
import json
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb
collection = db.artist
bulk = []
bulk_size = 10000

with gzip.open('artist.json.gz') as f:
    for line in f:
        data = json.loads(line)
        bulk.append(data)
        if len(bulk) == bulk_size:
            collection.insert_many(bulk)
            bulk = []

collection.create_index([('name', pymongo.ASCENDING)])  
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
