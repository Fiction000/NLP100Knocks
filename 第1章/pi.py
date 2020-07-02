pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_counts = []

# 文を単語へ分解
words_pi = pi.replace(',', '').strip('.').split(' ')
print(words_pi)

#単語の文字数を調べそのリストを作成
for word in words_pi:
    word_counts.append(len(word))

print(word_counts)
