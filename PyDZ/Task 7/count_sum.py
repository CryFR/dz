n = input('Введите число: ')
if all(map(str.isdigit, n)):
    n = list(map(int, n))
    flt = filter(lambda x: x % 2 != 0, n)
    print(sum(map(lambda x: x**2, flt)))
else:
    print('ВЫ должны ввести число, попробуйте еще раз!')
