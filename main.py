# Importing libraries
import random
import time

def create_dict(names, duplicateNames):
    random.seed(time.time())
    pairings = {}
    while (len(names) and len(duplicateNames)):
        person = random.choice(names)
        pair = random.choice(duplicateNames)
        while (person == pair and len(names) != 1):
            print(person + ", " + pair)
            person = random.choice(names)
            pair = random.choice(duplicateNames)
        pairings[person] = pair
        names.remove(person)
        duplicateNames.remove(pair)
    return pairings
