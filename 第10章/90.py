import word2vec

fname_vec = 'new_corpus_vec.bin'

model = word2vec.load(fname_vec)
print(model['United_States'])
indexes, similarities = model.cosine('England')
print(model.vocab[indexes])
indexes_ana, metrics_ana = model.analogy(pos=['Spain', 'Athens'], neg=['Madrid'], n=10)
print(model.vocab[indexes_ana])
