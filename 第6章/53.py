with open('nlp.txt.xml') as f:
    tokens = ''
    for line in f:
        if ('<word>' in line) or ('<lemma>' in line) or ('<CharacterOffsetBegin>' in line) or ('<CharacterOffsetEnd>' in line) or ('<POS>' in line) or ('<NER>' in line) or ('<Speaker' in line):
            tokens += line.strip(' ').strip('\n')
        elif '</token>' in line:
            print(tokens)
            tokens = ''
