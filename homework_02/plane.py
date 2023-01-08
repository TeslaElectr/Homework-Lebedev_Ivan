"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: float = 0, max_cargo: int = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if self.cargo + weight <= self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload("Перегрузка")

    def remove_all_cargo(self):
        cargo_value = self.cargo
        self.cargo = 0
        return cargo_value
