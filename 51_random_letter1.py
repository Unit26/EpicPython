import random


s = ['самовар', 'весна', 'лето']

x = random.choice(s)
lst = list(x)
rand = random.choice(lst)
i = lst.index(rand)
lst[i] = '?'
s2 = ''.join(lst)
print(s2)
r = input("Введите букву: ")
if r == rand:
    print("Победа!")
else:
    print("Попробуйте еще раз. Слово: ", x)
