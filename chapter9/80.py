import nltk

fname_read = 'enwiki-20150112-400-r100-10576.txt'
fname_write = 'corpus.txt'
sentences = []
symbols = '.,!?;:()[]\'\"'
with open(fname_read) as f, open(fname_write, 'w') as g:
    for sentence in f:
        tokens = nltk.word_tokenize(sentence)
        new_tokens = []
        for token in tokens:
            try:
                if token[0] in symbols:
                    token = token[1:]
                if token[-1] in symbols:
                    token = token[:-1]
                if token != '':
                    new_tokens.append(token)
            except IndexError:
                continue
        g.write(" ".join(new_tokens) + '\n')
