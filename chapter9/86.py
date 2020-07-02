from scipy import io
import pickle

''' 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．'''

fname_matrix_300 = 'matrix_300.mat'
fname_ts = 'ts.txt'
matrix_mat = io.loadmat(fname_matrix_300)
matrix = matrix_mat['mat300']

with open(fname_ts, 'r+b') as f:
    fts = pickle.load(f)

keys = list(fts)

print(matrix[keys.index('United_States')])
