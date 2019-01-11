import random
import tkinter
d = {'dog': 'собака', 'chair': 'стул', 'food': 'еда',
     'sun': 'солнце', 'life': 'жизнь', 'book': 'книга'}
word = random.choice(list(d.keys()))


def destroy():
    window.destroy()


def check():
    global word
    if d[word] == text.get().lower():
        label3.config(text='Правильно!')
        word = random.choice(list(d.keys()))
        label2.config(text=word)
        entry.delete(0, tkinter.END)

    else:
        label3.config(text='Ошибка!')


window = tkinter.Tk()
text = tkinter.StringVar()
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text='Случайное слово')
label.pack()
label2 = tkinter.Label(frame, text=word)
label2.pack()
entry = tkinter.Entry(frame, textvariable=text)
entry.pack()
label3 = tkinter.Label(frame, text='')
label3.pack()
button = tkinter.Button(frame, text='Готово!', command=check)
button.pack()
button2 = tkinter.Button(frame, text='Выход', command=destroy)
button2.pack()


window.mainloop()
