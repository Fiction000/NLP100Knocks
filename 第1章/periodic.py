'''

"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

'''

periodic = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
periodic_dict = {}
count = 1

# 文を単語へ分解
words_periodic = periodic.replace('.', '').split(' ')

#単語の先頭１，もしくは２文字を取り出し取り出した文字列から単語の位置への辞書を作成
for word in words_periodic:
    if count == 1 or count == 5 or count == 6 or count == 7 or count == 8 or    count == 9 or count == 15 or count == 16 or count == 19:
        periodic_dict[word[0]] = count
        count += 1
    else:
        periodic_dict[word[0:2]] = count
        count += 1

print(periodic_dict)
