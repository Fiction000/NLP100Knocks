import numpy as np
import operator

# sort hightemp.txt
# -*- coding: utf-8 -*-
data = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        data.append(row.replace('\t', ' ').strip())

new_data = []
words = []
for row in data:
    new_data.append(row.split(' '))
arr = np.array(new_data)

words,count = np.unique(arr[:, 0], return_counts=True)
uniques = dict(zip(words, count))
sorted_uniques = sorted(uniques.items(), key=operator.itemgetter(1), reverse=True)
for word in sorted_uniques:
    print(word[0])
