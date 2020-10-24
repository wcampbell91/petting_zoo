from animals.animals import Animal
from datetime import date

class Donkey(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
