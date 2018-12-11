from math import sqrt
L = [2, 4, 9, 16, 25]

l = [sqrt(x) for x in L]
print(l)

for i in L:
    print(sqrt(i))

def f(i):
    return sqrt(i)

print(list(map(f, L)))
