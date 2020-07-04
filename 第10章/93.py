'''92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．'''

fname_data_similarity = 'questions-words-family-similar.txt'
correct = 0
total = 0
with open(fname_data_similarity) as f:
    for line in f:
        tokens = line.split()
        if tokens[3] == tokens[4]:
            correct += 1
        total += 1

print(correct / total)
