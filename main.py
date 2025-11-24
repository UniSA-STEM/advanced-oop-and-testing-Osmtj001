'''
File: main.py
Description: This main module will allow for testing of the various functions & classes across this project. Common errors & incorrect input functions have been added
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''''

#Importing classes from other files
from staff import *
from enclosure import Enclosure
from Zoo import Zoo
from animal import *


#Normalizer to easily format functions upon output at a later stage
def normalizerformat(function, label):
    print('\n' + '=' * 30)
    print(f'{label}')
    print('=' * 30)
    function()
    input('\nPress Enter to continue...')




# Your Main.py file should act as a demonstra�on script. It does not need to be interac�ve, but
# it should clearly show how your system works by crea�ng objects, invoking methods, and
# prin�ng results. Think of it as a walkthrough of your zoo in ac�on.

def print_single_animal():
    zoo = Zoo("Michael's Sancutary")
    lion = Animal("Simba", "Lion", 5, "Meat", "Mammal", "Roar")
    print(lion)
#Attempting to add a Mammal to a Bird enclosure
def test_wrong_category():
    zoo = Zoo("Trent's Sanctuary")

    # Mammal in a Bird enclosure
    lion = Animal("Simba", "Lion", 5, "Meat", "Mammal", "Roar")
    bird_enclosure = Enclosure("Bird House", 40, "Aviary", "Bird")

    zoo.add_animal(lion)
    zoo.add_enclosure(bird_enclosure)


    bird_enclosure.add_animal(lion)


#Attempting to move animal into an enclosure while it has a health issue
def test_health_deny():
    zoo = Zoo("Trent's Sanctuary")

    penguin = Animal("Kowalski", "Penguin", 6, "Fish", "Bird", "Honk")
    penguin_pool = Enclosure("Penguin Pool", 60, "Aquatic", "Bird")

    zoo.add_animal(penguin)
    zoo.add_enclosure(penguin_pool)

    # Add a health issue
    leg_injury = Health("Leg injury", "2025-11-24", "High", "Rest for 3 days")
    penguin.add_health_issue(leg_injury)

    #Trying to add an animal that is under treatment
    penguin_pool.add_animal(penguin)   # should be blocked due to active issue

#Testing for Zookeeper not assigned to animal attempting to feed
def test_zookeeper_unassigned_animal():
    zoo = Zoo("Ryan's Sanctuary")

    a1 = Animal("Gloria", "Hippo", 7, "Hay", "Mammal", "Grunt")
    e1 = Enclosure("Hippo Pond", 120, "Aquatic", "Mammal")
    keeper1 = Zookeeper("Sam")
    keeper2 = Zookeeper("Riley")

    zoo.add_animal(a1)
    zoo.add_enclosure(e1)
    zoo.add_staff(keeper1)
    zoo.add_staff(keeper2)

    # Only Sam is assigned the animal and enclosure
    keeper1.assign_animal(a1)
    keeper1.assign_enclosure(e1)

    #Keeper1 feeding their assigned animal
    keeper1.feed_animal(a1)     # should work

    #Keeper2 trying to feed an animal they are NOT assigned to
    keeper2.feed_animal(a1)

def test_invalid_animal_input():
    zoo = Zoo("Davids's Sanctuary")
    e1 = Enclosure("Test Enclosure", 30, "Grassland", "Mammal")
    zoo.add_enclosure(e1)

    #Trying to add a string instead of an Animal object
    e1.add_animal("Not an animal")


#Full test of Zoo conditions, without planned errors
def test_zoo():
    zoo = Zoo("Bruce's Sanctuary")
#Creating Animal, Enclosure & Zookeeper
    a1 = Animal("Brax", "Penguin", 4, "Fish", "Bird", "Honk")
    e1 = Enclosure("Penguin Pool", 50, "Aquatic", "Bird")
    keeper = Zookeeper("Alex")

#Adding these animals to enclosures, and assigning zookeeper to animals
    zoo.add_animal(a1)
    zoo.add_enclosure(e1)
    zoo.add_staff(keeper)
    keeper.assign_enclosure(e1)
    keeper.assign_animal(a1)
    e1.add_animal(a1)

#Printing summary of Zoo, animals, enclosures & staff
    print("\n")
    print(zoo)
    zoo.list_animals()
    zoo.list_enclosures()
    zoo.list_staff()


#Calls the above functions with the formatting from Normalizer to return a clean output of test run
if __name__ == '__main__':
    normalizerformat(print_single_animal, "Print Summary for a single Animal")
    normalizerformat(test_wrong_category, "Attempting to add a Mammal to a Bird enclosure:")
    normalizerformat(test_health_deny, "Attempt to add animal under treatment to enclosure")
    normalizerformat(test_zookeeper_unassigned_animal, "Zookeeper feeding assigned vs unassigned animal")
    normalizerformat(test_invalid_animal_input, "Adding non-Animal to enclosure")
    normalizerformat(test_zoo, "Full test of Zoo functionality, no errors")