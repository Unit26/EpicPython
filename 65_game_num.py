import random
attempt = 3

x = random.randint(0, 10)
print("Компьютер загадал число. \nУ вас есть три попытки. Удачи!")
while attempt > 0:
    text = input("Попробуйте угадать: ")
    if text == "Выход":
        break
    else:
        num = int(text)
        if num == x:
            print("Победа!")
            break
        else:
            if num > x:
                print("Попробуйте число меньше!")
                attempt -= 1
                print("Попыток осталось: ", attempt)
            else:
                print("Попробуйте число больше!")
                attempt -= 1
                print("Попыток осталось: ", attempt)
