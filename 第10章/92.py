import word2vec

fname_data = 'questions-words-family.txt'
fname_data_similarity = 'questions-words-family-similar.txt'
fname_data_out = 'questions-words-family.bin'
fname_vec = 'context_words.bin'
fname_vec_out = 'corpus_similar.txt'
fname = 'context_words.txt'
fname_matrix_300 = 'matrix_300.mat'
fname_matrix_300_out = 'matrix_300_out.bin'

def word2vec_train(file_in, file_out):
    word2vec.word2vec(file_in, file_out, size=300, verbose=True)

# word2vec_train(fname_matrix_300, fname_matrix_300_out)
word2vec_train(fname, fname_vec)

# model1 = word2vec.load(fname_data_out)
# model2 = word2vec.load(fname_vec)

def w2v_calculate(file_in, file_out, model):
    with open(file_in) as f, open(file_out, 'w') as g:
        for line in f:
            tokens = line.split()
            try:
                index, metric = model.analogy(pos=[tokens[1], tokens[2]], neg=[tokens[0]], n=1)
            except IndexError:
                continue
            responses = model.generate_response(index, metric)
            word = responses[0][0]
            similarity = str(responses[0][1])
            g.write(line.strip('\n') + ' ' + word + ' ' + similarity + '\n')

w2v_calculate(fname, fname_vec_out, model2)
