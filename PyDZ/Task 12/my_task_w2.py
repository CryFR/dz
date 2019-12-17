# Упражнение 12.3

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


def show_tasks():
    text_output.configure(state='normal')
    text_output.delete(1.0, 'end')
    if list_of_tasks:
        text_output.insert('end',"Список задач:\n")
        for task in list_of_tasks:
            text_output.insert('end',f"Задача: {task['name']} "
                  f"| Категория: {task['category']} "
                  f"| Дата: {task['time']}\n")
    else:
        text_output.insert('end',"Список задач пуст")
    text_output.configure(state='disabled')

def put_task():
    new_task_name = entry_task.get().strip()
    new_task_cat = entry_category.get().strip()
    new_task_time = entry_time.get().strip()
    if new_task_name and new_task_cat and new_task_time:
        list_of_tasks.append({"name": new_task_name,
                              "category": new_task_cat,
                              "time": new_task_time})
    else:
        print("Не должно быть пустых полей")
    entry_task.delete(0, 'end')
    entry_category.delete(0, 'end')
    entry_time.delete(0, 'end')
    entry_task.focus()
    show_tasks()

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
window.geometry("{}x{}".format(700, 210))

# Frames
frame_user = tk.Frame(width=250)
frame_user.pack(anchor='w', fill='y', expand=False, side='left')
frame_user.grid_propagate(False)

frame_content = tk.Frame(window)
frame_content.pack(fill='both', expand=True, side='left')

# Labels
label_1 = tk.Label(frame_user, text="Задача:")
label_1.grid(row=0, column=0, padx=5, pady=5, sticky='e')

label_2 = tk.Label(frame_user, text="Категория:")
label_2.grid(row=1, column=0, padx=5, pady=5, sticky='e')

label_3 = tk.Label(frame_user, text="Дата:")
label_3.grid(row=2, column=0, padx=5, pady=5, sticky='e')

# Entries
entry_task = tk.Entry(frame_user)
entry_task.grid(row=0, column=1, padx=5, pady=5)

entry_category = tk.Entry(frame_user)
entry_category.grid(row=1, column=1, padx=5, pady=5)

entry_time = tk.Entry(frame_user)
entry_time.grid(row=2, column=1, padx=5, pady=5)

#Text
text_output = tk.Text(frame_content)
text_output.pack()

# Buttons
button_put_task = tk.Button(frame_user, text="Добавить эту задачу", command=put_task)
button_put_task.grid(row=3, column=1, padx=5, pady=5, sticky='e')

button_show_tasks = tk.Button(frame_user, text="Вывести список задач", command=show_tasks)
button_show_tasks.grid(row=4, column=1, padx=5, pady=5, sticky='e')

button_save = tk.Button(frame_user, text="Сохранить", command=save_tasks)
button_save.grid(row=5, columnspan=2, padx=5, pady=5)

button_quit = tk.Button(frame_user, text="Выход", command=window.destroy)
button_quit.grid(row=5, column=1, padx=5, pady=5, sticky='e')

#init
show_tasks()

window.mainloop()
