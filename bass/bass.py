from datetime import date

class Bass:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}")

    def __repr__(self):
        print(f"{self.name} is a {self.species} and was added on {self.date_added}")
