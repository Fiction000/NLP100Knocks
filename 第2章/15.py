# 15
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
# -*- coding: utf-8 -*-
# tail -4 hightemp.txt

n = int(input())
data = []
with open('hightemp.txt', 'r') as f:
    for row in f:
        data.append(row.replace('\t', ' ').strip())

for line in data[len(data) - n:]:
    print(line)
