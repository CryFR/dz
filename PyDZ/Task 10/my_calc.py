try:
    oper = input("Введите оператор: ")
    x, y = map(int, input("Введите два числа: ").split())
    if oper == "+":
        print(x + y)
    elif oper == "-":
        print(x - y)
    elif oper == "/":
        print(x // y)
    elif oper == "*":
        print(x * y)
    else:
        print(f"Операции '{oper}' не существует")
except ZeroDivisionError:
    print("/nДеление на ноль запрещено")

except ValueError:
    print("\nСледует ввести число!")
