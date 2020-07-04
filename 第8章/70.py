#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput, sys, random

pos = []
neg = []
with open('rt-polarity.pos', encoding = "ISO-8859-1") as f:
    for line in f:
        pos.append("+1 " + line)

with open('rt-polarity.neg', encoding = "ISO-8859-1") as f:
    for line in f:
        neg.append("-1 " + line)

posneg = pos + neg

loop = len(posneg)
with open('sentiment.txt', 'w') as f:
    for i in range(loop):
        f.write(posneg.pop(random.randrange(0, len(posneg))))

poscount = 0
negcount =0
with open('sentiment.txt') as f:
    for line in f:
        if '+1' in line:
            poscount +=  1
        else:
            negcount += 1

print(poscount, negcount, len(neg), len(pos))
