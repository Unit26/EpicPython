def call(x, y):
    if x == 343:
        return 15 * y
    elif x == 381:
        return 18 * y
    elif x == 473:
        return 13 * y
    elif x == 485:
        return 11 * y
    else:
        return 'невозможно определить. Выберите Екатеринбург, Омск, Воронеж или Ярославль '
<<<<<<< HEAD:25_call_tel.py.py
 
=======
>>>>>>> c83a52ca633b484506be747e890319bb17cf569f:2.5.py

x = int(input('Введите код города: '))
y = int(input('Введите длительность разговора: '))
print("Стоимость разговора: ", call(x, y))
