film = input("Выберите фильм(Пятница, Чемпионы, Пернатая банда): ")
date = input("Выберите дату(Сегодня, завтра): ")
time = int(input("Выберите время: "))
tickets = int(input("Укажите кол-во билетов: "))
price = 0





if tickets >= 20:
    price = price - (price * 0.2)
else:
    price = price - (price * 0.05)
print("Результ: {}  руб.".format(price))



