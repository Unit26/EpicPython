from math import pi
def fun(x):
    return f'Ответ: {pi:.{x}f}'


x = int(input('Сколько знаков после запятой? '))
print(fun(x))
