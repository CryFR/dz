from random import randint
rand_num = randint(1, 10)
num_of_tries = 3
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
i = 1
while i <= num_of_tries:
    guess = input(str(i) + '-я попытка: ')
    answer = int(guess)
    if guess == 'Выход':
        break
    elif answer > rand_num:
        print('Загаданное число меньше')
    elif answer < rand_num:
        print('Загаданное число больше')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', rand_num)
