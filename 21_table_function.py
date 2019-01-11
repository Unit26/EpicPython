def num_to_name(num):
    if num == 3:
        return 'Li - литий!'
    elif num == 17:
        return 'Cl - хлор!'
    elif num == 25:
        return 'Mn - марганец!'
    elif num == 80:
        return 'Hg - ртуть!'
    else:
        return ' NANI??????????'


num = int(input('Введите атомный номер: '))
print(num_to_name(num))
