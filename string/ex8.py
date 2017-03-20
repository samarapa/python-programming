def long_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][0]

print(long_word(["PHP", "Exercises", "Backend"]))
