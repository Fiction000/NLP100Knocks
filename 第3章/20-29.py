# coding: utf-8
import json
import re
from pprint import pprint
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

britain = str()
data =[]
with open('jawiki-country.json') as f:
    for line in f:
        data.append(json.loads(line))

for dicts in data:
    if dicts['title'] == u'イギリス':
        britain = dicts['text']
britain_list = britain.split('\n')

# 21
# # 記事中でカテゴリ名を宣言している行を抽出せよ．
# for line in britain_list:
#    if re.search(r'Category', line):
#         print(line)

# # 22
# # 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
# for line in britain_list:
#     category = re.compile(r'\[\[Category:(.*?)(\|.*?|\]\])')
#     s = category.search(line)
#     if s:
#         print(s.group(1))

# # 23
# # 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
# match1 = re.compile(r'^==(.*?)==')
# match2 = re.compile(r'^===(.*?)===')
# match3 = re.compile(r'^====(.*?)====')
# for line in britain_list:
#     if match3.match(line):
#         print(line.strip('====') + '3')
#     elif match2.match(line):
#         print(line.strip('===') + '2')
#     elif match1.match(line):
#         print(line.strip('==') + '1')

# # 24
# # 記事から参照されているメディアファイルをすべて抜き出せ．
# media = re.compile(ur'(File:|ファイル:)((.*?)(\.jpg|\.JPG))')
# for line in britain_list:
#     media_file = media.search(line)
#     if media_file:
#         print(media_file.group(2))

#
# 25-28
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
# basic_info = {}
# matchObj = re.compile(u"\|(?P<field>.*?)\s=\s(?P<value>.*?$)")
# for line in britain_list:
#     basic_info_template = matchObj.match(line)
#     if basic_info_template:
#         field_str = basic_info_template.group('field')
#         value_str = basic_info_template.group('value').replace("'", '').replace("\\", '').replace("<", '').replace(">", '').replace("ref", '').replace("|", '').replace("[", '').replace("]", '').replace("/", '')
#         print(field_str + ' ' + value_str)
#         basic_info[field_str] = value_str

#
# # 29
# #https://ja.wikipedia.org/w/api.php?format=xml&action=query&titles=File:Flag%20of%20the%20United%20Kingdom.svg&prop=imageinfo&iiprop=url

import requests
url = 'https://ja.wikipedia.org/w/api.php?format=xml&action=query&titles=File:Flag%20of%20the%20United%20Kingdom.svg&prop=imageinfo&iiprop=url&format=json'
result = requests.get(url).json()
print(result['query']['pages']['-1']['imageinfo'][0]['url'])
