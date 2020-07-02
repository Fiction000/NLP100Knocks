import random
import nltk

'''81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．'''


fname_corpus = 'new_corpus.txt'
fname_context_words = 'context_words.txt'
context_length = [1,2,3,4,5]

def context_words(file1, file2):
    with open(file1) as f, open(file2, 'w') as g:
        for line in f:
            tokens = nltk.word_tokenize(line)
            for i in range(len(tokens)):
                length = random.choice(context_length)
                try:
                    g.write(tokens[i] + "\t" + "\t".join(tokens[i-length:i]) + "\t" + "\t".join(tokens[i+1:i+length+1]) + "\n")
                except IndexError:
                    continue

context_words(fname_corpus, fname_context_words)
