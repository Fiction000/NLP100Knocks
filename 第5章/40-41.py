#!/usr/bin/python
# coding: utf-8

import CaboCha

class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

        def __str__(self):
        return self.surface + ',' + self.base + ',' + self.pos + ',' + self.pos1

class Chunk(Morph):
    def __init__(self, morphs):
        __init__().super()
        morphs = [Morph.surface, Morph.base, Morph.pos, Morph.pos1]
        dst = []
        srcs = []

    def __str__(self):
        return dst

def make_morph_list(parsed_text):
    '''解析された文書を，Morphオブジェクトのリストとして表現する'''
    sentence = []
    sentences = []
    with open(parsed_text) as f:
        for line in f:
            line_list = line.split()
            if '*' in line_list[0] or 'EOS' in line_list[0]:
                continue
            else:
                morph_list = line.replace('\t', ',').split(',')
                _morph = Morph(surface=morph_list[0], base=morph_list[7], pos=morph_list[1],
                pos1=morph_list[2])
                sentence.append(_morph)
                sentences.append(sentence)
                sentence = []
    return sentences

for morph in make_morph_list('neko.txt.cabocha')[2]:
    print(str(morph))

def make_chunk_list(parsed_text):
    '''解析された文書を，Chunkオブジェクトのリストとして表現する'''
    setence = []
    sentences = []
    with open(parsed_text) as f:
        for line in f:
            line_list = line.split()
            if 'EOS' in line_list[0]:
                continue
            elif '*' in line_list[0]:
                chunk_list = line.split()
                _chunk.dst.append(chunk_list[1])
                _chunk.srcs.append(chunk_list[2])
                chunk_list = []

print()
