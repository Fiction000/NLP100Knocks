import numpy as np

# sort -u col1.txt
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

for i in range(len(data)):
    if arr[i, 0] not in words:
        words.append(arr[i, 0])

print(words)
