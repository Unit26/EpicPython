def num_to_name(num):
    if num == 3:
        return 'Li - литий!'
    elif num == 25:
        return 'Mn - марганец!'
    elif num == 80:
        return 'Hg - ртуть!'
    elif num == 17:
        return 'Cl - хлор!'
    else:
        return ' NANI??????????'


num = int(input('Введите атомный номер: '))
print(num_to_name(num))
