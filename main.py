# Importing libraries
import random
import time
import csv

# Parsing the document
def parse_document():

    # Opening up the database
    with open('database.csv') as csv_file:

        # Configuring the dictionary and reader
        pairings = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        # Parsing through each line, adding to dictionary
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                pairings[row[0]] = row[1]
                line_count += 1
        
        # Returning the correct # of pairings
        return pairings

# Creating the dictionary and saving to the
def create_dict(names, duplicateNames):
    
    # Seeding and setting up dictionary
    random.seed(time.time())
    pairings = {}

    # Parsing through the list of names
    while (len(names) and len(duplicateNames)):

        # Creating random pair and person
        person = random.choice(names)
        pair = random.choice(duplicateNames)

        # Making sure pair and person are not same
        while (person == pair and len(names) != 1):
            print(person + ", " + pair)
            person = random.choice(names)
            pair = random.choice(duplicateNames)

        # Updating dictionary, removing respective names
        pairings[person] = pair
        names.remove(person)
        duplicateNames.remove(pair)
    
    # Saving to makeshift database
    with open('database.csv', mode='w') as database_file:
        database_writer = csv.writer(database_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Header
        database_writer.writerow(['Person', 'Match'])
        
        for key in pairings.keys():
            database_writer.writerow([key, pairings[key]])

    return pairings


names = ['Chris', 'Alyssa', 'Aidan', 'Summer', "Miguel", "Alex", "Caesar"]
create_dict(names, names.copy())