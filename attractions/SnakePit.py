from attractions.attraction import Attraction


class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
    
    def add_animal(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} has legs, don't add it to {self.attraction_name}")
