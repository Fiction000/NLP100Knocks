'''
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力

この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''

import string

# -*- coding: utf-8 -*-


def cipher(message):
    """与えられた文字列を暗号化，復号化する"""

    crypted = ""
    for c in message:
        if c in string.ascii_lowercase:
            crypted += chr(219 - ord(c))
        else:
            crypted += c
    return crypted


message = "Verweile doch! Du bist so schön."
print(cipher(message))
print(cipher(cipher(message)))
