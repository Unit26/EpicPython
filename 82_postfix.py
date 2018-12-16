s = input('Калькулятор: ')
lst = s.split()
stack = []
for x in lst:
    if x.isdigit():
        stack.append(x)
    else:
        a = int(stack.pop())
        b = int(stack.pop())
        if x == '*':
            c = a * b
            stack.append(c)
        elif x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '/':
            stack.append(a / b)
        elif x == '//':
            stack.append(a // b)
        elif x == '**':
            stack.append(a ** b)
        print(stack)