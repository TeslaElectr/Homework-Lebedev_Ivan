"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.cargo = 0
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo <= self.max_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload("Перегрузка")

    def remove_all_cargo(self):
        cargo_value = self.cargo
        self.cargo = 0
        return cargo_value
