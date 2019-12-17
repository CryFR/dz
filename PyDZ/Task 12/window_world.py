from tkinter import *
import random

root = Tk()

words = {
        'Cat':'кошка',
        'Dog':'собака',
        'Cow':'корова'
        }
word = random.choice(list(words.keys()))
def check():
    try:
        if entry.get() == words[word]:
            label_guess.config(text='Угадал')
        else:
            label_guess.config(text='Не угадал')
    except:
        label_guess.config(text='Ошибка ввода!')

label_header = Label(text='Случайное слово:')
label_rand = Label(text=word)
label_trans = Label(text='Укажите перевод слова:')
entry = Entry()
label_guess = Label()
confirm_butt = Button(text='Погнали!', command=check)
exit_butt = Button(root, text='Выход', command=root.destroy)

label_header.pack()
label_rand.pack()
label_trans.pack()
entry.pack()
label_guess.pack()
confirm_butt.pack()
exit_butt.pack()
root.mainloop()