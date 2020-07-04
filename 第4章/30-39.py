import operator
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

'''
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

mecab_dict = {}
mecab_list2 = []
morph_list = []
with open('neko.txt.mecab') as f:
    for line in f:
        # 空白，改行の時を除外
        if 'EOS' in line:
            continue
        if '\u3000' in line:
            continue
        # 形態素の辞書を作成し，一文ごとにリストに入れる
        else:
            try:
                mecab_list = line.replace('\t', ',').split(',')
                mecab_dict['surface'] = mecab_list[0]
                mecab_dict['pos'] = mecab_list[1]
                mecab_dict['pos1'] = mecab_list[2]
                mecab_dict['base'] = mecab_list[7]
            except IndexError:
                continue
        mecab_list2.append(mecab_dict)
        if '。' in mecab_dict.values():
            morph_list.append(mecab_list2)
            mecab_list2 = []
        mecab_dict = {}

# 31
# 動詞の表層形をすべて抽出せよ．
# for morphs in morph_list:
#     for morph in morphs:
#         if '動詞' in morph.values():
#             print(morph['surface'])

# 32
# 動詞の原形をすべて抽出せよ．
# for morphs in morph_list:
#     for morph in morphs:
#         if '動詞' in morph.values():
#             print(morph['base'])

# 33
# サ変接続の名詞をすべて抽出せよ．
#for morphs in morph_list:
#    for morph in morphs:
#        if ('サ変接続' in morph.values()) and ('名詞' in morph.values()):
#            print(morph['surface'])

# 34
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
# i = 0
# for morphs in morph_list:
#     for morph in morphs:
#         if ('の' in morph.values()):
#             if ('名詞' in morphs[i-1].values()) and ('名詞' in morphs[i+1].values()):
#                 print(morphs[i-1]['surface'] + morph['surface'] + morphs[i+1]['surface'])
#         i += 1
#     i = 0

# 35
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
# i = 0
# length = 0
# noun_consecs = ''
# for morphs in morph_list:
#     for morph in morphs:
#         if ('名詞' in morph.values()):
#             if ('名詞' in morphs[i+1].values()):
#                 # 最長の名詞連接を見つける
#                 if (len(morphs[i]['surface']) + len(morphs[i+1]['surface']) > length):
#                     length = (len(morphs[i]['surface']) + len(morphs[i+1]['surface']))
#                     noun_consecs = (morphs[i]['surface'] + morphs[i+1]['surface'])
#         i += 1
#     i = 0
# print(noun_consecs)

# 36
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
occurances = {}
for morphs in morph_list:
    for morph in morphs:
        if morph['surface'] not in occurances.keys():
            occurances[morph['surface']] = 0
        occurances[morph['surface']] += 1

sorted_occurances = sorted(occurances.items(), key=operator.itemgetter(1), reverse=True)

# 37
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
plot_occurances = []
plot_words = []
for occ in sorted_occurances[0:10]:
    plot_words.append(occ[0])
    plot_occurances.append(occ[1])
# print(plot_occurances)
# plt.bar(arange(10), plot_occurances)
# ylabel('word occurances')
# show()

# 38
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
kinds = []
occs = []
for num in sorted_occurances:
    occs.append(num[1])
for num in occs:
    kinds.append(occs.count(num))
#plt.hist(occs, 50)

# 39
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
plt.plot([math.log(c) for c in occs], [math.log(c) for c in range(1, len(occs)+1)], 'o')
show()
