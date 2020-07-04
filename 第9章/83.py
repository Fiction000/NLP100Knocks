# coding: utf-8
import nltk
import pickle
from collections import Counter
'''82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数'''

fname = 'context_words.txt'
fname_ftcs = 'ftcs.txt'
fname_ts = 'ts.txt'
fname_cs = 'cs.txt'

cooccurances = Counter()
t_occurances = Counter()
c_occurances = Counter()

with open(fname) as f:
    for line in f:
        tokens = line.strip('\n').split('\t')
        for i in range(1, len(tokens)):
            cooccurances.update([tokens[0] + '\t' + tokens[i]])
            t_occurances.update([tokens[0]])
            c_occurances.update([tokens[i]])
with open(fname_ftcs, 'w+b') as f:
    pickle.dump(cooccurances, f)
with open(fname_ts, 'w+b') as f:
    pickle.dump(t_occurances, f)
with open(fname_cs, 'w+b') as f:
    pickle.dump(c_occurances, f)
