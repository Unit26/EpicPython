l = []
while True:
    print('Простой todo: \n  1. Добавить задачу. \n  2. Вывести список задач. \n  3. Выход. \n')
    text = int(input('Введите число: '))
    if text == 3:
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
        break
    elif text == 1:
        a = input('Сформулируйте задачу: ')
        b = input('Добавьте категорию: ')
        c = input('Добавьте дату: ')
        l.append({'Задание: ': a, 'Категория: ': b, 'Дата: ': c})
    else:
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
