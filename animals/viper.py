from datetime import date

class Viper:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")

    def __repr__(self):
        print(f"{self.name} is a {self.species} and was added to the zoo on {self.date_added}")
