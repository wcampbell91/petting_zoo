from movements.swimming import Swimming
from movements.walking import Walking
from animals.animals import Animal
from datetime import date

class Gorilla(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
