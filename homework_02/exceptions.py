"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, text):
        self.text = text



class NotEnoughFuel(Exception):
    def __init__(self, text):
        self.text = text


class CargoOverload(Exception):
    def __init__(self, text):
        self.text = text


