import word2vec

fname_vec = 'new_corpus_vec.bin'

model = word2vec.load(fname_vec)
print(model['United_States'])
indexes, similarities = model.cosine('country')
model.generate_response(indexes, similarities).tolist()
