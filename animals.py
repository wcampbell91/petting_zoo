from datetime import date
from anaconda import Anaconda
from bass import Bass
from cobra import Cobra
from copperhead import Copperhead
from donkey import Donkey
from goat import Goat
from gorilla import Gorilla
from great_white import Great_White
from llama import Llama
from mini_horse import Mini_Horse
from perch import Perch
from piranha import Piranha
from platypus import Platypus
from rattle_snake import Rattle_Snake
from viper import Viper
from attractions.PettingZoo import PettingZoo
from attractions.SnakePit import SnakePit
from attractions.Wetlands import Wetlands


fuzzy = Llama("fuzzy", "Classic Llama", "morning", "llama food")
burro = Donkey("burro", "Amiatina", "midday", "donkey food")
lil_sebastian = Mini_Horse("lil' Sebastian", "Noma Pony", "night", "hay")
billy = Goat("Billy", "Mountain Goat", "morning", "grass")
joe = Gorilla("joe", "Silverback", "midday", "babies")
slippy = Copperhead("Slippy", "Copperhead", "mouse")
sloppy = Cobra("Sloppy", "King Cobra", "mouse")
slinky = Anaconda("Slinky", "Anaconda", "Mouse")
sleuthy = Viper("Sleuthy", "Russell's Viper", "mouse")
sneaky = Rattle_Snake("Sneaky", "Rattle Snake", "mouse")
charles = Piranha("Charles", "Red-bellied Piranha", "fingers")
bob = Perch("Bob", "Eurasian Perch", "fish food")
gene = Bass("Gene", "White Bass", "fish food")
jaws = Great_White("Jaws", "Great White", "innocent swimmers")
bill = Platypus("Bill", "Duck-billed Platypus", "snickers bars")

print('*************')

# PettingZoo.add_animal(fuzzy)
# PettingZoo.add_animal(burro)
# PettingZoo.add_animal(lil_sebastian)
# PettingZoo.add_animal(billy)
# PettingZoo.add_animal(joe)

# SnakePit.add_animal(slippy)
# SnakePit.add_animal(sloppy)
# SnakePit.add_animal(slinky)
# SnakePit.add_animal(sleuthy)
# SnakePit.add_animal(sneaky)

# Wetlands.add_animal(charles)
# Wetlands.add_animal(bob)
# Wetlands.add_animal(gene)
# Wetlands.add_animal(jaws)
# Wetlands.add_animal(bill)

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

for animal in varmint_village.animals:
    print(f"You'll find {animal.name}, the {animal.species} in {varmint_village.attraction_name}")

print('***********')

for animal in slithery_sleuths.animals:
    print(f"You'll find {animal.name}, the {animal.species} in {slithery_sleuths.attraction_name}")

print('***********')

for animal in rascal_lake.animals:
    print(f"You'll find {animal.name}, the {animal.species} in {rascal_lake.attraction_name}")
