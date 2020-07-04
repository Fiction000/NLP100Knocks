from sklearn.decomposition import TruncatedSVD
from scipy import io

fname_matrix = 'matrix.txt.mat'
fname_matrix_300 = 'matrix_300'
matrix_mat = io.loadmat(fname_matrix)
matrix = matrix_mat['matrix']
svd = TruncatedSVD(300)
matrix_300 = svd.fit_transform(matrix)
io.savemat(fname_matrix_300,{'mat300': matrix_300})
