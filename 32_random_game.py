import random


def fun():
    return random.randint(1, 4)


def fun1(y):
    if y == x:
        return 'Победа!'
    else:
        if y < x:
            return 'Поворите еще раз! Ваше число меньше нужного'
        else:
            return 'Поворите еще раз! Ваше число больше нужного'


x = fun()


y = int(input('Введите число: '))


print(fun1(y))
