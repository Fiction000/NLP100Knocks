with open('nlp.txt.xml') as f:
    token = []
    tokens = []
    for line in f:
        if ('<word>' in line) or ('<lemma>' in line) or ('<CharacterOffsetBegin>' in line) or ('<CharacterOffsetEnd>' in line) or ('<POS>' in line) or ('<NER>' in line) or ('<Speaker' in line):
            token.append(line.strip(' ').strip('\n'))
        elif '</token>' in line:
            tokens.append(token)
            token = []

print(tokens[3][5])

for token in tokens:
    if 'PERSON' in token[5]:
        print(token[0])
