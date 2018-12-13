total = 0
while True:
    x = input('Введите число или Стоп для выхода: ')
    if x.lower() == "стоп":
        print("Сумма введенных чисел: ", total)
        break
    elif x.isdigit():
        total += int(x)
    else:
        print("Ошибка ввода")
