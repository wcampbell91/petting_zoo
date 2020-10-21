from datetime import date

class Goat:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}")

    def __repr__(self):
        print(f"{self.name} is a {self.species} and was added to the zoo on {self.date_added}")
