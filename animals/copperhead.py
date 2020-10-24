from animals.animals import Animal
from datetime import date

class Copperhead(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
