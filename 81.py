from random import randint
lst = [randint(-10, 10) for _ in range(20)]

print(lst)
max_sum = sum(lst[0:5])
max_i = lst[0]
print(max_i)
for i in range(len(lst)-5):
    tmp_srez = lst[i:i+5]
    tmp_sum = sum(tmp_srez)
    if tmp_sum > max_sum:
        max_sum = tmp_sum
        max_i = i

print([lst[i] for i in range(max_i, max_i+5)])
