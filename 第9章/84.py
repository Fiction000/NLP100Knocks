# coding: utf-8
import math
import pickle
from collections import Counter
from collections import OrderedDict
from scipy import sparse, io

fname_ftcs = 'ftcs.txt'
fname_ts = 'ts.txt'
fname_cs = 'cs.txt'
fname_matrix = 'matrix.txt'

with open(fname_ftcs, 'r+b') as f:
    ftcs = pickle.load(f)
with open(fname_ts, 'r+b') as f:
    fts = pickle.load(f)
with open(fname_cs, 'r+b') as f:
    fcs = pickle.load(f)

N = sum(ftcs.values())

dict_index_t = OrderedDict((key, i) for i, key in enumerate(fts.keys()))
dict_index_c = OrderedDict((key, i) for i, key in enumerate(fcs.keys()))

matrix = sparse.lil_matrix((len(fts), len(fcs)))

for key,f_tcs in ftcs.items():
    if f_tcs >= 10:
        tokens = key.split('\t')
        t = tokens[0]
        c = tokens[1]
        matrix[dict_index_t[t], dict_index_c[c]] = max(math.log((N * f_tcs) / (fts[t] * fcs[c])), 0)

# 結果の書き出し
io.savemat(fname_matrix, {'matrix': matrix})
