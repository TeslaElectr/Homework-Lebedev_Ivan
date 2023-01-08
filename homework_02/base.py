from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption):

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


if __name__ == '__main__':
    v = Vehicle()
    print(v.started)
    v.start()
    print(v.started)
    v.move(12.4)
    print(f'{v.fuel=}')
