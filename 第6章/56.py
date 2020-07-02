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

def sentence2word(sentences):
    words = []
    for sentence in sentences:
        matchObj = re.split(r'\s', sentence)
        if matchObj:
            for word in matchObj:
                words.append(word)
    return words

sentences = text2sentence('nlp.txt.xml')
words = sentence2word(sentences)

with open('nlp.txt') as f:
    token = []
    tokens = []
    for line in f:
        if ('<mention' in line) or ('<text>' in line):
            token.append(line.strip(' ').strip('\n'))
        elif '</mention>' in line:
            tokens.append(token)
            token = []

print(tokens)

rep_dict = {}
value = ''
for token in tokens:
    if token[0] == '<mention>':
        rep_dict[token[1].strip('<text>').strip('</text>')] = value
    if 'true' in token[0]:
        value = token[1].strip('<text>').strip('</text>')

print(rep_dict)

with open('nlp.txt') as f:
    for line in f:
        if
