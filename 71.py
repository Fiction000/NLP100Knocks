stopwords = []
with open('stopwords.txt') as f:
    """http://xpo6.com/list-of-english-stop-words/より"""
    for line in f:
        stopwords.append(line.strip('\n'))

print(stopwords)


def stopword_or_not(word):
    if word in stopwords:
        return True
    return False

print(stopword_or_not('I'))
print(stopword_or_not('among'))
print(stopword_or_not('me'))
print(stopword_or_not('Me'))
