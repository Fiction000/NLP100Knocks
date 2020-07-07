'''
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
'''

import random
# -*- coding: utf-8 -*-


def typoglycemia(sentence):
    """文中の各単語について，先頭と末尾の文字は残し，他の文字をランダムに並び替える"""

    words = sentence.replace(',', '').replace(':', '').strip('.').split(' ')
    random_word = ""
    for i in range(len(words)):
        if len(words[i]) > 4:
            for j in range(len(words[i][1:-1])):
                random_word += words[i][1:-
                                        1][random.randrange(0, len(words[i][1:-1]))]
            words[i] = (words[i][0] + random_word + words[i][-1])
            random_word = ""
    return words


print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
