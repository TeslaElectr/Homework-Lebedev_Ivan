from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=1000, fuel=50, fuel_consumption=6):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Недостаточно топлива для запуска")

    def move(self, distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel("Не хватает топлива")


    def __str__(self) -> str:
        return self.__class__.__name__


    def __repr__(self) -> repr:
        return str(self) 


if __name__ == '__main__':
    v = Vehicle(weight=1000, fuel=50, fuel_consumption=4)
    print(v)
    print(v.started)
    v.start()
    print(v.started)
    v.move(12.4)
    print(f'{v.fuel=}')
    v.move(0.06)
    print(f'{v.fuel=}')