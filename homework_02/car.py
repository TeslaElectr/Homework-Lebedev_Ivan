"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle
from engine import Engine


class Car(Vehicle):
    engine = None

    # def __init__(self, engine, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.engine = engine

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: float = 0, engine: Engine = None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine
