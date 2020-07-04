from stemming.porter2 import stem
import nltk
import numpy as np

stopwords = []
features = []

with open('stopwords.txt') as f:
    """http://xpo6.com/list-of-english-stop-words/より"""
    for line in f:
        stopwords.append(line.strip('\n'))

def stopword_or_not(word):
    if word in stopwords:
        return True
    return False

review_without_stopwords = []
with open('sentiment.txt') as f:
    for line in f:
        for word in line[3:].split(' '):
            if word in stopwords:
                continue
            elif word == '\n' or word == ';':
                continue
            else:
                features.append(stem(word))

with open('features.txt', 'w') as f:
    for word in features:
        f.write(word + '\n')
