from sklearn.metrics.pairwise import cosine_similarity
from scipy import io
import pickle

fname_matrix_300 = 'matrix_300.mat'
fname_ts = 'ts.txt'
matrix_mat = io.loadmat(fname_matrix_300)
matrix = matrix_mat['mat300']

with open(fname_ts, 'r+b') as f:
    fts = pickle.load(f)

keys = list(fts)

print(cosine_similarity(matrix[keys.index('United_States')], matrix[keys.index('U.S')]))
