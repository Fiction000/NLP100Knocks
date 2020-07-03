import leveldb
import gzip
import json

fname = 'artist.json.gz'
fname_db = 'test_db'

# LevelDBオープン、なければ作成
db = leveldb.LevelDB(fname_db)

with gzip.open(fname, 'rb') as f:
    for line in f:
        json_data = json.loads(line)
        key = json_data['name']
        value = json_data.get('area')
        if value == None:
            value = ''
        db.Put(key.encode(), value.encode())

print(db.Get("Al Street".encode()).decode())
