import datetime

# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

# Properties
    # designer - It will hold your name.
    # date_constructed - This will hold the exact time the building was created.
    # owner - This will store the same of the person who owns the building.
    # address
    # stories

class Building:

    def __init__(self, address, stories):
        self.designer = "Ryan Cunningham"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

# Methods
# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

    def construct(self):
        self.date_constructed = datetime.datetime.now()

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

    def purchase(self, owner):
        self.owner += owner

# Constructor
# Define your __init__ method to accept two arguments

    # address
    # stories
# Once defined this way, you can send those values as parameters when you create each instance

#  eight_hundred_eighth = Building("800 8th Street", 12)

# Creating Your Buildings
# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

Building1 = Building("100 First Street", 1)
Building2 = Building("200 Second Street", 2)
Building3 = Building("300 Third Street", 3)
Building4 = Building("400 Fourth Street", 4)
Building5 = Building("500 Fifth Street", 5)

Building1.purchase("Willam Von Weelden")
Building1.construct()

for prop, value in Building1.__dict__.items():
    print(f'{prop}:\n{value}\n')