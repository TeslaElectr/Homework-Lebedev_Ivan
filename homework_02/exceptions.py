"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, number):
        self.text = 'Не хватает топлива для запуска'
        self.number = number


class NotEnoughFuel(Exception):
    def __init__(self, number):
        self.text = 'Недостаточно топлива'
        self.number = number


class CargoOverload(Exception):
    def __init__(self, number):
        self.text = 'Перегрущка'
        self.number = number

