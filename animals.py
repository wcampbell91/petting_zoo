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

fuzzy = Llama("fuzzy", "Classic Llama", "morning")
burro = Donkey("burro", "Amiatina", "midday")
lil_sebastian = Mini_Horse("lil' Sebastian", "Noma Pony", "night")
billy = Goat("Billy", "Mountain Goat", "morning")
joe = Gorilla("joe", "Silverback", "midday")
slippy = Copperhead("Slippy", "Copperhead")
sloppy = Cobra("Sloppy", "King Cobra")
slinky = Anaconda("Slinky", "Anaconda")
sleuthy = Viper("Sleuthy", "Russell's Viper")
sneaky = Rattle_Snake("Sneaky", "Rattle Snake")
charles = Piranha("Charles", "Red-bellied Piranha")
bob = Perch("Bob", "Eurasian Perch")
gene = Bass("Gene", "White Bass")
jaws = Great_White("Jaws", "Great White")
bill = Platypus("Bill", "Duck-billed Platypus")
print(f"{joe.name} is a {joe.species} and is on the {joe.shift} shift!")
