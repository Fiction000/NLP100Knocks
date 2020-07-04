from sklearn.metrics.pairwise import cosine_similarity
from scipy import io
import operator
import pickle

fname_matrix_300 = 'matrix_300.mat'
fname_ts = 'ts.txt'
matrix_mat = io.loadmat(fname_matrix_300)
matrix = matrix_mat['mat300']

with open(fname_ts, 'r+b') as f:
    fts = pickle.load(f)

keys = list(fts)

similar_to_target = {}
for key in keys:
    target_vector = matrix[keys.index('Spain')] - matrix[keys.index('Madrid')] + matrix[keys.index('Athens')]
    similarity = cosine_similarity(target_vector, matrix[keys.index(key)])[0][0]
    similar_to_target[key] = similarity

sorted_similar = sorted(similar_to_target.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_similar[0:9])
