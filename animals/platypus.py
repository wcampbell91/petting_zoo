from movements.walking import Walking
from movements.swimming import Swimming
from animals.animals import Animal
from datetime import date

class Platypus(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
