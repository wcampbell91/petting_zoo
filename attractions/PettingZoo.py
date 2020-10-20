class PettingZoo:
    def __init__(self,name,description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        print(f"{self.attraction_name}: {self.description}")
