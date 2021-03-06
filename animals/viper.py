from movements.swimming import Swimming
from movements.slithering import Slithering
from animals.animals import Animal
from datetime import date

class Viper(Animal, Slithering, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
