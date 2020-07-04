import word2vec
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold
from matplotlib import pyplot as plt

fname_vec = 'new_corpus_vec.bin'

model = word2vec.load(fname_vec)
indexes, similarities = model.cosine('country', n=100)
array = model.generate_response(indexes, similarities)
print(model.vocab[indexes])
vectors_list =  []

for name in array:
    vectors_list.append(model[name[0]])

fig = plt.figure(figsize=(15, 8))
vectors_related_to_country = np.array(vectors_list)
tsne = manifold.TSNE(n_components=2, init="random", random_state=0)
Y = tsne.fit_transform(vectors_related_to_country)
plt.scatter(Y[:, 0], Y[:, 1], cmap=plt.cm.Spectral)
plt.title('t-SNE visualization of word vectors')
plt.axis('tight')

plt.show()
