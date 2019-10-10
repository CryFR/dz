with open('moby_clean.txt') as file:
    words = {}
    for word in file:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
print(word, words)
