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

print(collection.find({'name' : "Queen"}))
