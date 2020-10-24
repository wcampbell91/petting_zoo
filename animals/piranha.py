from movements.swimming import Swimming
from animals.animals import Animal
from datetime import date

class Piranha(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
