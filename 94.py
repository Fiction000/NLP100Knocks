import word2vec
import numpy as np
from scipy import io
import pickle

fname_in = 'combined.tab'
fname_out = 'combined_phrase.bin'
fname_txt_out = 'combined.txt'
fname_mat = 'matrix_300.mat'
fname_ts = 'ts.txt'
matrix_300 = io.loadmat(fname_mat)['mat300']


with open(fname_ts, 'r+b') as f:
    fts = pickle.load(f)

keys = list(fts)

def cosine_similarity(X, Y):
    normXY = np.linalg.norm(X) * np.linalg.norm(Y)
    if normXY != 0:
        result = (np.dot(X, Y)) / (np.linalg.norm(X) * np.linalg.norm(Y))
    else:
        return -1
    return result

def cosine_similarity_calculate(file_in, file_out, matrix, word_list):
    with open(file_in) as f, open(file_out, 'w') as g:
        for line in f:
            tokens = line.split('\t')
            try:
                similarity = cosine_similarity(matrix[word_list.index(tokens[0])], matrix[word_list.index(tokens[1])])
            except ValueError:
                similarity = -1
            g.write(line.strip('\n') +  ' ' + str(similarity) + '\n')

cosine_similarity_calculate(fname_in, fname_txt_out, matrix_300, keys)
