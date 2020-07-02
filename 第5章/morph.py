# coding: utf-8
import MeCab

class Morph(object):
    def __init__(self, text):
        self.text    = text
        self.surface = []
        self.base    = []
        self.pos     = []
        self.pos1    = []

    def parse_mecab(self):
        '''入力された文書をMeCabで形態素解析する'''
        mecab = MeCab.Tagger('')
        mecab_dict = {}
        morph_list = []
        with open(self.text) as f:
            for line in f:
                node = mecab.parse(line)
                mecab_arr = node.split('\n')
                for mecab_words in mecab_arr:
                    mecab_arr2 = mecab_words.replace('\t', ',').split(',')
                    if '\u3000' in mecab_arr2[0] or mecab_arr2[0] == '' or mecab_arr2[0] == 'EOS':
                        continue
                    else:
                        try:
                            mecab_dict['surface'].append(mecab_arr2[0])
                            mecab_dict['pos'].append(mecab_arr2[1])
                            mecab_dict['pos1'].append(mecab_arr2[2])
                            mecab_dict['base'].append(mecab_arr2[6])
                        except KeyError:
                            mecab_dict['surface'] = [mecab_arr2[0]]
                            mecab_dict['pos'] = [mecab_arr2[1]]
                            mecab_dict['pos1'] = [mecab_arr2[2]]
                            mecab_dict['base'] = [mecab_arr2[6]]
                        if '。' in mecab_arr2[0]:
                            self.surface.append(mecab_dict['surface'])
                            self.base.append(mecab_dict['base'])
                            self.pos.append(mecab_dict['pos'])
                            self.pos1.append(mecab_dict['pos1'])
                            mecab_dict = {}


    def getSurface(self):
        return self.surface

    def getBase(self):
        return self.base

    def getPos(self):
        return self.pos

    def getPos1(self):
        return self.pos1


morph = Morph('neko.txt.cabocha')
morph.parse_mecab()
print(morph.getSurface()[2])
print(morph.getBase()[2])
print(morph.getPos()[2])
print(morph.getPos1()[2])
