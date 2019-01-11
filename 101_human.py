class Human:
    def __init__(self, newName="Без имени"):
        self._name = newName
        self._age = 0

    def eating(self):
        print(self._name, 'ест')

    def sleeping(self):
        print(self._name, 'спит')

    def working(self):
        if 18 <= self._age < 65:
            print(self._name, 'работает')
        elif self._age >= 65:
            print(self._name, 'на пенсии')

    def relaxing(self):
        print(self._name, 'отдыхает')

    def growing(self):
        print(self._name, 'отмечает день рождения')
        self._age += 1


class Life:
    def life(self, human, years=70):
        while years:
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1


petr = Human('Петр')

life_petr = Life()
life_petr.life(petr)
