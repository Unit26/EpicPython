def my_max(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2


value1 = int(input('Введите первое число: '))
value2 = int(input('Введите второе число: '))

print(my_max(value1, value2))
