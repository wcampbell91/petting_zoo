from datetime import date

class Cobra:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} at {date.today()}")

    def __repr__(self):
        print(f"{self.name} is a {self.sepecies} and was added to the zoo on {self.date_added}")
