import heapq
with open('moby_clean.txt') as file:
    words = {}
    for word in file:
        word = word.strip()
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    del words['']
print(f"Пять самых частых слов: {heapq.nlargest(5, words, key=words.get)}\nПять самых редких слов: {heapq.nsmallest(5, words, key=words.get)}")
