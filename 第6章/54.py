with open('nlp.txt.xml') as f:
    tokens = ''
    for line in f:
        if ('<word>' in line) or ('<lemma>' in line) or ('<POS>' in line):
            tokens += line.strip(' ').strip('\n') + '\t'
        elif '</token>' in line:
            print(tokens)
            tokens = ''
