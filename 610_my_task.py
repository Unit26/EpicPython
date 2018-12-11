l = []
while True:
    text = int(input('Простой todo: \n  1. Добавить задачу. \n  2. Вывести список задач. \n  3. Выход. \n' ))
    if text == 3:
        break
    elif text == 1:
        a = input('Сформулируйте задачу: ')
        b = input('Добавьте категорию: ')
        c = input('Добавьте дату: ')
        l.append("Задача:" + a + " Категория:" + b + " Дата:" + c)
    else:
        print(l)
        
  
