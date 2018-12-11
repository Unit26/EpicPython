import random
attempt = 3
def fun():
    return random.randint(0, 10)

x = fun()
print("Компьютер загадал число. \nУ вас есть три попытки. Удачи!" )
while attempt > 0:
    text = input("Попробуйте угадать: ")
    if text == "Выход":
        break
    else:
        int(text)
        if text == x:
            print("Победа!")
        else:
            if text > x:
                print("Попробуйте число меньше!")
                attempt -= 1
                print("Попыток осталось: ", attempt)
            else:
                print("Попробуйте число больше!")
                attempt -= 1
                print("Попыток осталось: ", attempt)
