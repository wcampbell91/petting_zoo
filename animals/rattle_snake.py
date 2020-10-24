from movements.swimming import Swimming
from movements.slithering import Slithering
from animals.animals import Animal
from animals.anaconda import Anaconda
from datetime import date

class Rattle_Snake(Animal, Slithering, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Swimming.__init__(self)
