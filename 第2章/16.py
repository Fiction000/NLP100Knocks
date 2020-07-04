# 16
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

# -*- coding: utf-8 -*-
# head -4 hightemp.txt

n = int(input())
data = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        data.append(row.replace('\t', ' ').strip())

partition_point = len(data) // n
print(partition_point)
partitioned_data = []
start = 0
while True:
    if partition_point > len(data):
        break
    partitioned_data.append(data[start:partition_point])
    start += partition_point
    print(start)
    partition_point *= 2
    print(partition_point)

print(partitioned_data)
