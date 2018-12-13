from math import sqrt


L = [2, 4, 9, 16, 25]

l = [sqrt(x) for x in L]
print(l)

l2 = []
for i in L:
    x = sqrt(i)
    l2.append(x)
print(l2)

print(list(map(lambda i: sqrt(i), L)))
