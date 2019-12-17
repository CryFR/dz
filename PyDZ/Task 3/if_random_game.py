import random
ran = random.randint(0, 4)
guess = int(input('Угадайте чилос от 1-4: '))
if ran == guess:
    print('Победа')
else:
    print('Повтори еще раз')
