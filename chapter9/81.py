import nltk
'''英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．'''



fname_corpus = 'corpus.txt'
fname_countries = 'country.txt'
fname_new_corpus = 'new_corpus.txt'
new_country_dict = {}

def make_country_dict(file):
    country_dict = {}
    with open(file) as g:
        for line in g:
            tokens = line[0:-6].split(' ')
            if len(tokens) >= 2:
                country_dict.setdefault(tokens[0], [])
                country_dict[tokens[0]].append(tokens[1:])
    return country_dict

country_dict = make_country_dict(fname_countries)

def make_corpus(file1, file2):
    skip = 0
    with open(file1) as f, open(file2, 'w') as g:
        for line in f:
            result = []
            tokens = nltk.word_tokenize(line)
            for i in range(len(tokens)):
                try:
                    for name in country_dict[tokens[i]]:
                        try:
                            if tokens[tokens.index(tokens[i])+1] == name[0]:
                                result.append(tokens[i] + '_' + '_'.join(name))
                                skip = len(name)
                        except IndexError:
                            continue
                except KeyError:
                    if skip > 0:
                        skip -= 1
                        continue
                    else:
                        result.append(tokens[i])
            g.write(" ".join(result) + '\n')

make_corpus(fname_corpus, fname_new_corpus)
