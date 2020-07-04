import leveldb
import gzip
import json

fname_db = 'test_db'

# LevelDBオープン、なければ作成
db = leveldb.LevelDB(fname_db)

area = 'Japan'.encode()
count = 0
for value in db.RangeIter():
    if value[1] == area:
        count += 1
print(count)
