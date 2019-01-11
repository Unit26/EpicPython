def full_price(film, time, num_tickets):
    if film == 'Пятница':
        if time == 12:
            return 250 * num_tickets
        elif time == 16:
            return 350 * num_tickets
        elif time == 20:
            return 450 * num_tickets
    elif film == 'Чемпионы':
        if time == 10:
            return 250 * num_tickets
        elif time == 13:
            return 350 * num_tickets
        elif time == 16:
            return 350 * num_tickets
    elif film == 'Пернатая банда':
        if time == 10:
            return 350 * num_tickets
        elif time == 14:
            return 450 * num_tickets
        elif time == 18:
            return 450 * num_tickets
    else:
        return 'Ошибка ввода.'


def final_price(day, num_tickets, x):
    if num_tickets >= 20:
        if day == 'сегодня':
            return x * 0.80
        elif day == 'завтра':
            return x * 0.75
    else:
        if day == 'сегодня':
            return x
        elif day == 'завтра':
            return x * 0.95
        else:
            return 'Ошибка ввода.'


film = input('Выбрать фильм: ')
day = input('Выбрать день: ')
time = int(input('Выбрать время: '))
num_tickets = int(input('Выбрать количество билетов: '))
x = full_price(film, time, num_tickets)
print("Результат: ", final_price(day, num_tickets, x))
