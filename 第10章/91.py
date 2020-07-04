fname = 'questions-words.txt'
fname_output = 'questions-words-family.txt'
family_or_not = False

with open(fname) as f, open(fname_output, 'w') as g:
    for line in f:
        if 'family' in line:
            family_or_not = True
        if ':' in line and 'family' not in line:
            family_or_not = False
        if family_or_not == True and 'family'not in line:
            g.write(line)
