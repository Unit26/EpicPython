s = input("Введите число: ")
total = sum([int(x)**2 for x in s if int(x) % 2 != 0])
print(total)
