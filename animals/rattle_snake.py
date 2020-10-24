from animals.animals import Animal
from animals.anaconda import Anaconda
from datetime import date

class Rattle_Snake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
