list_of_tasks = dict()
i = 0
while True:
    choice = int(input('''1. Добавить задачу.
2. Вывести список задач.
3. Выход.
Укажите число:  '''))
    if choice == 1:
        list_of_tasks['new_task%d' % i] = input('Сформулируйте задачу: ')
        list_of_tasks['new_cat%d' % i] = input('Добавьте категорию к задаче: ')
        list_of_tasks['new_time%d' % i] = input('Добавьте время к задаче: ')
        i += 1
    elif choice == 2:
        for j in range(i):
            print("\nЗадача: {}; Категория: {}; Дата: {}\n".format(list_of_tasks['new_task%d' % j], list_of_tasks['new_cat%d' % j], list_of_tasks['new_time%d' % j]))
    elif choice == 3:
        break
