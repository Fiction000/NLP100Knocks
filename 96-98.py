import word2vec
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

fname_vec = 'new_corpus_vec.bin'

model = word2vec.load(fname_vec)
indexes, similarities = model.cosine('country', n=100)
array = model.generate_response(indexes, similarities)
print(model.vocab[indexes])
vectors_list =  []

for name in array:
    vectors_list.append(model[name[0]])

vectors_related_to_country = np.array(vectors_list)
# kmeans = KMeans(n_clusters=5).fit(vectors_related_to_country)
# print(kmeans.labels_)


Z = linkage(vectors_related_to_country, 'ward')

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering of Country')
plt.xlabel('index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,
    leaf_font_size=8.,
)
plt.show()
