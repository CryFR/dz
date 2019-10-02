sum = 0
while True:
    attempt = input('Введите число("Стоп" для окончания ввода): ')
    if all(map(str.isdigit, attempt)):
        sum += int(attempt)
    elif attempt == 'Стоп':
        break
print(f'Сумма числе равна {sum}')
