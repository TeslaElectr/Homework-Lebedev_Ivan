"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle
from engine import Engine


class Car(Vehicle):

    def __init__(self, engine=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine
