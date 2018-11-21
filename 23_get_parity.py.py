def fun(x):
    if  x % 2 == 0:
        return ' чётное '
    else:
        return ' нечётное '


x = int(input('Введите число: '))
print(fun(x))
