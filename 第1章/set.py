'''
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

from n_gram import ngram

str1 = "paraparaparadise"
str2 = "paragraph"

# bi-gramの集合を作成
X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

# 和集合，積集合，差集合
print(X | Y)
print(X & Y)
print(X - Y)

# 'se'はXおよびYに含まれるか？
print('se' in X)
print('se' in Y)
