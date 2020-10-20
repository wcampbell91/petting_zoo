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

print(bill)
