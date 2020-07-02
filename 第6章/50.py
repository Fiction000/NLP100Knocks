import re
from stemming.porter2 import stem


def text2sentence(text):
    with open(text) as f:
        sentences = []
        sentence = ''
        for line in f:
            matchObj = re.split(r'[.;:\?!]\s[A-Z]', line)
            if matchObj:
                sentence += matchObj[0]
                sentences.append(sentence)
                if len(matchObj) > 2:
                    sentences.append(matchObj[1])
                    sentence = matchObj[2]
                else:
                    try:
                        sentence = matchObj[1]
                    except IndexError:
                        sentence = ''
            else:
                sentence += line
    return sentences

sentences = text2sentence('nlp.txt.xml')

def sentence2word(sentences):
    words = []
    for sentence in sentences:
        matchObj = re.split(r'\s', sentence)
        if matchObj:
            for word in matchObj:
                words.append(word)
    return words

words = sentence2word(sentences)

def stemming(words):
    for word in words:
        print(word + '  ' + stem(word))
