import doctest


def calc(s):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''
    lst = s.split()
    stack = []
    for x in lst:
        if x.isdigit():
            stack.append(x)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if x == '*':
                stack.append(b * a)
            elif x == '+':
                stack.append(b + a)
            elif x == '-':
                stack.append(b - a)
    return str(stack[0])


doctest.testmod()
s = input('Калькулятор: ')
result = calc(s)
print(result)
