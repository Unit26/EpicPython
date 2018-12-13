l = []
while True:
    print('Простой todo: \n  1. Добавить задачу. \n  2. Вывести список задач. \n  3. Выход. \n')
    text = int(input('Введите число: '))
    if text == 3:
        break
    elif text == 1:
        a = input('Сформулируйте задачу: ')
        b = input('Добавьте категорию: ')
        c = input('Добавьте дату: ')
        l.append([a, b, c])
        #l.append("Задача:" + a + " Категория:" + b + " Дата:" + c)
    else:
        for x in l:
            a, b, c = x
            print("Задача: " + a + " Категория: " + b + " Дата: " + c)
