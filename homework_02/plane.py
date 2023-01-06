"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo: int = 5, max_cargo: int = 1000, *args, **kwargs):
        self.cargo = cargo
        self.max_cargo = max_cargo
        super().__init__(*args, **kwargs)

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo <= self.max_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload("Перегрузка")

    def remove_all_cargo(self):
        cargo_value = self.cargo
        self.cargo = 0
        return cargo_value
