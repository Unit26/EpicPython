s = "У лукоморья 123 дуб зеленый 456"
s.find("я") #1
s.count("у") #2
if s.isalpha() == True: #3
    print(True)
else:
    print(s.upper())


if len(s) > 4:  #4
    print(s.lower())
else:
    print(len(s))


s.replace("У", "О") #5
