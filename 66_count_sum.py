s = int(input())
total = 0
for i in range(len(str(s))):
    if s[i] % 2 == 0:
        continue
    total = total + int(s[i]**2)

print("Сумма: ", total)
        
