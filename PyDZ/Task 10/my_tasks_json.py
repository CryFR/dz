# Упражнение 10.9

def reader(filename):
    """
    Чтение содержимого json файла
    """
    from json import load
    with open(filename) as f_obj:
        content = load(f_obj)
    return content


def writer(filename, content):
    """
    Запись в json файл
    json.dump(content, file)
    """
    from json import dump
    try:
        with open(filename, 'w') as f_obj:
            dump(content, f_obj)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        list_of_tasks = list(reader('tasks.json'))
        print(f"Текущие задачи:\n{list_of_tasks}")
    except FileNotFoundError:
        print("Файл не найден\nСоздаем новый список задач")
        list_of_tasks = []
    except Exception as e:
        print(e)
        list_of_tasks = []

    while True:
        try:
            print("\nпростой todo:\n"
                "    1. Добавить задачу.\n"
                "    2. Вывести список задач.\n"
                "    3. Выход.\n")
            choice = input("Укажите число: ")

            if choice == '1':
                new_task_name = input("Сформулируйте задачу: ")
                new_task_cat = input("Добавьте категорию к задаче: ")
                new_task_time = input("Добавьте время к задаче: ")
                if new_task_name and new_task_cat and new_task_time:
                    list_of_tasks.append({"name": new_task_name,
                                        "category": new_task_cat,
                                        "time": new_task_time})

            elif choice == '2':
                if list_of_tasks:
                    for task in list_of_tasks:
                        print(f"Задача: {task['name']}"
                              f"| Категория: {task['category']}"
                              f"| Дата: {task['time']}")
                else:
                    print("Список задач пуст")

            elif choice == '3':
                writer("tasks.json", list_of_tasks)
                print("Файл записан успешно")
                break
        except:
            continue
