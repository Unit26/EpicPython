import tkinter

import json


def reader(filename):
    try:
        with open(filename) as f_obj:
            tasks = json.load(f_obj)
            return tasks
    except Exception as e:
        print(e)
        return []


def writer(filename, tasks):
    try:
        with open(filename, 'w') as f_obj:
            json.dump(tasks, f_obj)
    except Exception as e:
        print(e)


def add_task():
    l.append({'Задание: ': a.get(), 'Категория: ': b.get(), 'Дата: ': c.get()})
    entry.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)


def show_task():
    text.delete(1.0, tkinter.END)
    for x in l:
        for c in x:
            text.insert(tkinter.END, c + x[c] + '\n')


def breaking():
    writer('todo.json', l)
    print('Задания записаны. ')
    window.destroy()


l = reader('todo.json')


window = tkinter.Tk()
a = tkinter.StringVar()
b = tkinter.StringVar()
c = tkinter.StringVar()

main_frame = tkinter.Frame(window)
main_frame.pack(side='left')
main_frame2 = tkinter.Frame(window)
main_frame2.pack(side='right')
frame = tkinter.Frame(main_frame)
frame.pack()
label = tkinter.Label(frame, text='Задача ')
label.pack(side='left')
entry = tkinter.Entry(frame, textvariable=a)
entry.pack(side='right')
frame2 = tkinter.Frame(main_frame)
frame2.pack()
label2 = tkinter.Label(frame2, text='Категория')
label2.pack(side='left')
entry2 = tkinter.Entry(frame2, textvariable=b)
entry2.pack(side='right')
frame3 = tkinter.Label(main_frame)
frame3.pack()
label3 = tkinter.Label(frame3, text='Время')
label3.pack(side='left')
entry3 = tkinter.Entry(frame3, textvariable=c)
entry3.pack(side='right')
frame4 = tkinter.Frame(main_frame)
frame4.pack()
button = tkinter.Button(frame4, text='Добавить задачу', command=add_task)
button.pack()
button2 = tkinter.Button(
    frame4, text='Вывести список задач', command=show_task)
button2.pack()
button3 = tkinter.Button(frame4, text='Выход', command=breaking)
button3.pack()

text = tkinter.Text(main_frame2, width=100, height=20)
text.pack()
window.mainloop()
