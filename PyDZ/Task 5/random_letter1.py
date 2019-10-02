import random
mas = ['самовар', 'весна', 'лето']
word = random.choice(mas)
randlett = random.choice(word)
wordspl = list(word)
ind = word.index(randlett)
wordspl[ind] = '?'
print("".join(wordspl))
guess = str(input('Введите букву: '))
if guess == randlett:
    print("Победа!")
else:
    print("Увы! Попробуй в другой раз.")