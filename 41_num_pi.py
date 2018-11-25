from math import pi
num = pi
def fun(x):
    return f'{num:.xf}'


x = int(input('Сколько знаков после запятой? '))
print(fun(x))
