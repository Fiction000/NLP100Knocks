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

dance_list = []

for dance in collection.find({'tags.value' : "dance"}).sort('rating.count', pymongo.DESCENDING):
    dance_list.append(dance)

print(dance_list[0:10])
