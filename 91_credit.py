def money_reader(what, when):
    import csv
    reg = {}
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            # delimiter по умолчанию ','
            money_reader = csv.reader(csvfile, delimiter=',')
            for row in money_reader:
                if row[0] == what and when in row[2]:
                    if row[1] not in reg:
                        reg[row[1]] = [int(row[3])]
                    else:
                        reg[row[1]].append(int(row[3]))
        reg.pop('Россия')
        for key in reg.keys():
            reg[key] = sum(reg[key])
        print(reg)
        max_value = 0
        max_reg = ''
        for key, value in reg.items():
            if value > max_value:
                max_value = value
                max_reg = key

        return max_reg, max_value

    except Exception as e:
        return e


if __name__ == '__main__':
    year = 2017
    what = 'Количество заявок на потребительские кредиты'
    print(money_reader(what, str(year)))
