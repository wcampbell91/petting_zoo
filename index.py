from animals import Anaconda, Bass, Cobra, Copperhead, Donkey, Goat, Gorilla, Great_White, Llama, Mini_Horse, Perch, Piranha, Platypus, Rattle_Snake, Viper
from attractions import PettingZoo, SnakePit, Wetlands

fuzzy = Llama("fuzzy", "Classic Llama", "morning", "llama food", 54654312)
burro = Donkey("burro", "Amiatina", "midday", "donkey food", 654135)
lil_sebastian = Mini_Horse("lil' Sebastian", "Noma Pony", "night", "hay", 656544)
billy = Goat("Billy", "Mountain Goat", "morning", "grass", 487946)
joe = Gorilla("joe", "Silverback", "midday", "babies", 6543887)
slippy = Copperhead("Slippy", "Copperhead", "mouse", 8797546)
sloppy = Cobra("Sloppy", "King Cobra", "mouse", 6854925)
slinky = Anaconda("Slinky", "Anaconda", "Mouse", 951645)
sleuthy = Viper("Sleuthy", "Russell's Viper", "mouse", 75395146)
sneaky = Rattle_Snake("Sneaky", "Rattle Snake", "mouse", 982573)
charles = Piranha("Charles", "Red-bellied Piranha", "fingers", 64654984)
bob = Perch("Bob", "Eurasian Perch", "fish food", 341586)
gene = Bass("Gene", "White Bass", "fish food", 1654958)
jaws = Great_White("Jaws", "Great White", "innocent swimmers", 9879321)
bill = Platypus("Bill", "Duck-billed Platypus", "snickers bars", 13216848)

varmint_village = PettingZoo("Varmint Village", "Here at Varmint Village you'll pet the world")
rascal_lake = Wetlands("Rascal Lake", "Swim with the fishes, and be alive!")
slithery_sleuths = SnakePit("Slithery Sleuths", "Nobody told you there'd be snakes")

varmint_village.add_animal(fuzzy)
varmint_village.add_animal(burro)
varmint_village.add_animal(lil_sebastian)
varmint_village.add_animal(billy)
varmint_village.add_animal(joe)

slithery_sleuths.add_animal(slippy)
slithery_sleuths.add_animal(sloppy)
slithery_sleuths.add_animal(slinky)
slithery_sleuths.add_animal(sleuthy)
slithery_sleuths.add_animal(sneaky)

rascal_lake.add_animal(charles)
rascal_lake.add_animal(bob)
rascal_lake.add_animal(gene)
rascal_lake.add_animal(jaws)
rascal_lake.add_animal(bill)

# for animal in varmint_village.animals:
#     print(f"You'll find {animal.name}, the {animal.species} in {varmint_village.attraction_name}")

# print('***********')

# for animal in slithery_sleuths.animals:
#     print(f"You'll find {animal.name}, the {animal.species} in {slithery_sleuths.attraction_name}")

# print('***********')

# for animal in rascal_lake.animals:
#     print(f"You'll find {animal.name}, the {animal.species} in {rascal_lake.attraction_name}")

# print(charles.chip_num)
for animal in varmint_village.animals:
    print(f"{animal.name} is in here!")
