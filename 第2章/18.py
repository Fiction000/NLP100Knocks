import numpy as np

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

print(np.sort(arr)[::-1])
