# Упражнение 12.2

import tkinter as tk
import os.path


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
    with open(filename, 'w') as f_obj:
        dump(content, f_obj)


def save_tasks():
    try:
        writer('tasks.json', list_of_tasks)
        print("Файл записан успешно")
    except Exception as e:
        print(e)


def get_tasks():
    if list_of_tasks:
        print("Список задач:")
        for task in list_of_tasks:
            print(f"Задача: {task['name']} "
                  f"| Категория: {task['category']} "
                  f"| Дата: {task['time']}")
    else:
        print("Список задач пуст")


def put_task():
    new_task_name = entry_task.get().strip()
    new_task_cat = entry_category.get().strip()
    new_task_time = entry_time.get().strip()
    if new_task_name and new_task_cat and new_task_time:
        list_of_tasks.append({"name": new_task_name,
                              "category": new_task_cat,
                              "time": new_task_time})
    entry_task.delete(0, 'end')
    entry_category.delete(0, 'end')
    entry_time.delete(0, 'end')
    entry_task.focus()

# Chek for file and init list of tasks
if os.path.exists('tasks.json'):
    print("Сохраненный список найден")
    try:
        list_of_tasks = list(reader('tasks.json'))
        print("Загрузка списка успешна")
    except Exception as e:
        print(e)
else:
    print("Файл не найден\n"
          "Создание нового списка задач")
    list_of_tasks = []

# tkinter
window = tk.Tk()
window.title("Упражнение 12.2")

# Frames
user_frame = tk.Frame()
user_frame.pack(anchor='w', fill='y', expand=False, side='left')

# Labels
label_1 = tk.Label(user_frame, text="Задача:")
label_1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

label_2 = tk.Label(user_frame, text="Категория:")
label_2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

label_3 = tk.Label(user_frame, text="Дата:")
label_3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

# Entries
entry_task = tk.Entry(user_frame)
entry_task.grid(row=0, column=1, padx=5, pady=5)

entry_category = tk.Entry(user_frame)
entry_category.grid(row=1, column=1, padx=5, pady=5)

entry_time = tk.Entry(user_frame)
entry_time.grid(row=2, column=1, padx=5, pady=5)

# Buttons
button_put_task = tk.Button(user_frame, text="Добавить эту задачу", command=put_task)
button_put_task.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

button_get_tasks = tk.Button(user_frame, text="Вывести список задач", command=get_tasks)
button_get_tasks.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)

button_save = tk.Button(user_frame, text="Сохранить", command=save_tasks)
button_save.grid(row=5, columnspan=2, padx=5, pady=5)

button_quit = tk.Button(user_frame, text="Выход", command=window.destroy)
button_quit.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

window.mainloop()
