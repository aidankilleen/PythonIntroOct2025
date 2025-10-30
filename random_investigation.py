# random_investigation.py

#from random import choice, randint, shuffle

# it is possible but not recommended to use a wildcard import
from random import *


r = randint(1, 10)
print(r)

people = ["Alice", "Bob", "Carol", "Dan", "Eve", "Fred", "Ger"]

chosen_person = choice(people)
print(chosen_person)

shuffle(people)
print(people)






