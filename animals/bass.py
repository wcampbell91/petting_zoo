from datetime import date

class Bass:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
        self.__chip_num = chip_num

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, number):
        pass

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}")

    def __repr__(self):
        print(f"{self.name} is a {self.species} and was added on {self.date_added}")
