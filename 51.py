import random
s = ['самовар', 'весна', 'лето']
x = random.choice(s)
lst = list(x)                                                                  
rand = random.choice(lst)
i = lst.index(rand)
lst[i] = '?'
print(lst)

r = print(input("Введите букву: "))
def f(r, i):
    if r == rand:
        print("Победа!")
    else:
        print("Попробуйте еще раз. Слово: ", x)
