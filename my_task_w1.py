import tkinter
l = []


def breaking():
    def writer(filename, tasks):
        import json
        try:
            with open(filename, 'w') as f_obj:
                json.dump(tasks, f_obj)
        except Exception as e:
            print(e)

    if __name__ == "__main__":
        writer('todo.json', l)
    print('Задания записаны. ')


def task():
    l.append({'Задание: ': a, 'Категория: ': b, 'Дата: ': c})


def tasksprint():
    for x in l:
        for c in x:
            print(c, x[c])

    def reader(filename):
        import json
        try:
            with open(filename) as f_obj:
                tasks = json.load(f_obj)
                return tasks
        except Exception as e:
            return e
    if __name__ == "__main__":
        print(reader('todo.json'))

a = tkinter.StringVar()
b = tkinter.StringVar()
c = tkinter.StringVar()

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text = 'Задача ')
label.pack(side = 'left')
entry = tkinter.Entry(frame, textvariable = a)
entry.pack(side = 'right')
frame2 = tkinter.Frame(window)
frame2.pack()
label2 = tkinter.Label(frame2, text = 'Категория')
label2.pack(side = 'left')
entry2 = tkinter.Entry(frame2, textvariable = b)
entry2.pack(side = 'right')
frame3 = tkinter.Label(window)
frame3.pack()
label3 = tkinter.Label(frame3, text = 'Время')
label3.pack(side = 'left')
entry3 = tkinter.Entry(frame3, textvariable = c)
entry3.pack(side = 'right')
frame4 = tkinter.Frame(window)
frame4.pack()
button = tkinter.Button(frame4, text = 'Добавить задачу', command = task)
button.pack()
button2 = tkinter.Button(
    frame4, text = 'Вывести список задач', command = tasksprint)
button2.pack()
button3 = tkinter.Button(frame4, text = 'Выход', command = breaking)
button3.pack()
window.mainloop()
