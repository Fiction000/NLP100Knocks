# coding: utf-8
# 16
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

# -*- coding: utf-8 -*-
# split -4 hightemp.txt

n = int(input())
data = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        data.append(row.replace('\t', ' ').strip())

split_data = []
split_point = n
start = 0
while True:
    split_data.append(data[start:split_point])
    start += n
    split_point += n
    if split_point > len(data):
        break

print(len(split_data))
