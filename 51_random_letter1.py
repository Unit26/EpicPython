import random


def f(r, i):
    if r == rand:
        print("Победа!")
    else:
        print("Попробуйте еще раз. Слово: ", x)


s = ['самовар', 'весна', 'лето']

x = random.choice(s)
lst = list(x)
rand = random.choice(lst)
i = lst.index(rand)
lst[i] = '?'
s2 = ''.join(lst)

r = print(input("s2 \n Введите букву: "))
