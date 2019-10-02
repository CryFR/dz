print('Фильм «Пятница»,\n'
      'сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб.\n'
      'Фильм «Чемпионы»,\n'
      'сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб.\n'
      'Фильм «Пернатая банда»,\n'
      'сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб.\n'
      'от 20 человек - скидка 20%,\n'
      'заказ за день до сеанса - скидка 5%\n')

film = str(input("Выберите фильм(Пятница, Чемпионы, Пернатая банда): ").lower())
date = input("Выберите дату(Сегодня, завтра): ")
s_time = str(input("Выберите время: "))
tickets = int(input("Укажите кол-во билетов: "))
price = 0

if film == "пятница":
    if s_time == '12':
        price += 250
    elif s_time == '16':
        price += 350
    elif s_time == '20':
        price += 450

elif film == 'чемпионы':
    if s_time == '10':
        price += 250
    elif s_time == '13':
        price += 350
    elif s_time == '16':
        price += 350

elif film == 'пернатая банда':
    if s_time == '10':
        price += 350
    elif s_time == '14':
        price += 450
    elif s_time == '18':
        price += 450

if tickets >= 20:
    price = price - (price * 0.2)
else:
    price = price - (price * 0.05)

if price != 0:
    print('Выбран фильм:', film, '| День:', date,
          ' | Время:', s_time, ' | Количество билетов:',
          tickets,'\nРезультат: {} руб.'.format(price))
else:
    print("Ошибка ввода")


