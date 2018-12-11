s = "У лукоморья 123 дуб зеленый 456"
print(s.find("я")) #1
print(s.count("у")) #2
if s.isalpha() == False: #3
    print(s.upper())


if len(s) > 4:  #4
    print(s.lower())


new_s = "О" + s[1:] #5
print(new_s)
