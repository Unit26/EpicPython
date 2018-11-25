def fun(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s


s = input('Ваша строка: ')
n = int(input('Число: '))
print(fun(s, n))
