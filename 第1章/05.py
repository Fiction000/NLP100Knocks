'''
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''

def ngram(seq, n):
    """与えられたシーケンスのn-gramを作る"""
    n_gram = []
    for i in range(len(seq)):
        if len(seq[i:n + i]) < n:
            continue
        else:
            n_gram.append(seq[i:n + i])
    return n_gram


NLPer = "I am an NLPer"
NLPer_words = NLPer.split(' ')
print(ngram(NLPer, 2))
print(ngram(NLPer_words, 2))
