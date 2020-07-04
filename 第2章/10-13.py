import numpy as np

# -*- coding: utf-8 -*-
data = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        data.append(row.replace('\t', ' ').strip())

# 10
# wc -l hightemp.txtt
print(len(data))

# 11
# sed s/\\t/\ /g hightemp.txt
print(data)

# 12
# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')
new_data = []
for row in data:
    new_data.append(row.split(' '))
arr = np.array(new_data)

for i in arr[:, 0]:
    col1.write(i + '\n')
for i in arr[:, 1]:
    col2.write(i + '\n')

# 13
# paste col1.txt col2.txt
col1 = open('col1.txt')
col2 = open('col2.txt')
col12 = open('col12.txt', 'w')

col1l = []
col2l = []
for line in col1:
    col1l.append(line.replace('\n', '\t'))
for line in col2:
    col2l.append(line)
for line1, line2 in zip(col1l, col2l):
    col12.write(line1 + line2)
