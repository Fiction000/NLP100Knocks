import leveldb
import gzip
import json

fname = 'artist.json.gz'
fname_db = 'artist_tag_db'

db = leveldb.LevelDB(fname_db)

# with gzip.open(fname, 'rb') as f:
#     for line in f:
#         json_data = json.loads(line)
#         key = json_data['name']
#         value = []
#         tags = json_data.get('tags')
#         if tags == None:
#             value = ''
#         else:
#             for tag in tags:
#                 value.append(tag['value'])
#         db.Put(key.encode(), json.dumps([value, len(value)]).encode())

print(db.Get("Pablo Sciuto".encode()).decode())
