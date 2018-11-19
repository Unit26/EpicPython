def fun(a,b,c,d):
    if a == 'Пятница' :
        if c == 12:
            if b == 'сегодня':
                if d >= 20:
                    return 250 * 0.8
                else:
                    return 250
            elif b == 'завтра':
                if d >= 20:
                    return 250 * 0.75
                else:
                    return 250 * 0.95
        elif c == 16:
            if b == 'сегодня':
                if d >= 20:
                    return 350 * 0.8
                else:
                    return 350
            elif b == 'завтра':
                if d >= 20 :
                    return 350 * 0.75
                else:
                    return 350 * 0.95
        elif c == 20:
            if b == 'сегодня':
                if d >= 20:
                    return 450 * 0.8
                else:
                    return 450
            elif b == 'завтра':
                if d >= 20 :
                    return 450 *0.75
                else:
                    return 450 *0.95
    elif a == 'Чемпионы' :
        if c ==10:
            if b == 'сегодня':
                if d >= 20:
                    return 250 * 0.8
                else:
                    return 250
            elif b == завтра:
                if d >= 20:
                    return 250 * 0.75
                else:
                    return 250 * 0.95
        elif c == 13:
            if b == 'сегодня':
                if d >= 20:
                    return 350 * 0.8
                else:
                    return 350
            elif b == 'завтра':
                if d >= 20 :
                    return 350 * 0.75
                else:
                    return 350 * 0.95
        elif c == 16:
            if b == 'сегодня':
                if d >= 20:
                    return 350 * 0.8
                else:
                    return 350
            elif b == 'завтра':
                if d >= 20 :
                    return 350 * 0.75
                else:
                    return 350 * 0.95
    elif a == 'Пернатая банда' :
        if c ==10:
            if b == 'сегодня':
                if d >= 20:
                    return 350 * 0.8
                else:
                    return 350
            elif b == 'завтра':
                if d >= 20:
                    return 350 * 0.75
                else:
                    return 350 * 0.95
        
        elif c == 14:
            if b == 'сегодня':
                if d >= 20:
                    return 450 * 0.8
                else:
                    return 450
            elif b == 'завтра':
                if d >= 20 :
                    return 450 *0.75
                else:
                    return 450 *0.95
        elif c == 18:
            if b == 'сегодня':
                if d >= 20:
                    return 450 * 0.8
                else:
                    return 450
            elif b == 'завтра':
                if d >= 20 :
                    return 450 *0.75
                else:
                    return 450 *0.95
    else:
        return 'Ошибка ввода.'


a = input('Выбрать фильм: ')
b = input('Выбрать день: ')
c = int(input('Выбрать время: '))
d = int(input('Выбрать количество билетов: '))
print ("Результат: ", fun(a, b , c , d))
                
