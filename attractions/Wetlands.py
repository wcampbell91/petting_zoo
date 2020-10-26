from attractions.attraction import Attraction


class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")

        except AttributeError as ex:
            print(f"{animal} can't swim, so please do not put it in {self.attraction_name}")
