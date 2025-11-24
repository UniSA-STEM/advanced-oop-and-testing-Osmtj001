''''
File: enclosure.py
Description: This module allows the Enclosure class to be instantiated. This class allows for values name, size, environment, animal, cleanliness & animals
Getters & Setters are used to ensure only the correct data is permitted into the function
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''

#Enclosure Class represents a habitat for animals within the zoo. It holds values such as name, size, environment type, animal type, cleanliness, and animals housed within.
class Enclosure:
#Required Properties for this class. These properties are validated through a setter to ensure that the correct value type is inputted before running
    def __init__(self, name, size, environment, animal_type):
        self.name = name
        self.size = size
        self.__environment = environment
        self.__animal_type = animal_type
        self.cleanliness = 100
        self.__animal = []

#Getters & Setters for various variables. These functions perform the same, if not very similar task of ensuring the data is validated before being entered into the class. If the incorrect data is entered, an error will print and a default value is assigned.
    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        if isinstance(name, str) and name is not None:
            self.__name = name
            print(f"Enclosure name: {name}")
        else:
            self.__name = "Default Enclosure"
            print(f"Enclosure name did not meet requirements: {self.__name} has been assigned")


    def __get_size(self):
        return self.__size

    def __set_size(self, size):
        if isinstance(size, int) and size is not None and size > 0:
            self.__size = size
            print(f"Enclosure size: {size}")
        else:
            self.__size = 0
            print(f"Enclosure size did not meet requirements. Size has been defaulted to {self.__size}")

    def __get_environment(self):
        return self.__environment

    def __get_animal_type(self):
        return self.__animal_type

    def __get_cleanliness(self):
        return self.__clean

    def __set_cleanliness(self, clean):
        if isinstance(clean, int) and  0 <= clean <=100:
            self.__clean = clean
            print(f"Enclosure cleanliness: {self.__clean}")
        else:
            self.__clean = 0
            print(f"Enclosure was not cleaned")
#Returns a copy of the animal list
    def __get_animals(self):
        return list(self.__animal)

#Adds an animal to this enclosure if conditions are met
#Animal must not have active health issue
#Animal category must match enclosure animal type
#Must pass data validation
#If not, an error is returned
    def add_animal(self, animal):
        if not isinstance(animal, str):
            if animal.has_active_issues():
                print(f"{animal.name} has an active health issues & cannot be added to an enclosure")
                return

            if animal.category == self.__animal_type:
                self.__animal.append(animal)
                print(f"Added animal: {animal.name} to enclosure {self.name}")

            else:
                print(f"This enclosure is for {self.__animal_type} animals only.")

        else:
            print(f"Invalid animal object given. Please enter a string representing an animal")
#Checks to see if the animal exists within the enclosure. If so, it is removed
    def remove_animal(self, animal):
        if not isinstance(animal, str) and animal in self.__animal:
            self.__animal.remove(animal)
            print(f"Removed animal: {animal} from Enclosure {self.name}")

#Lists all current animals within this enclosure
    def list_animals(self):
        if len(self.__animal) > 0:
            for a in self.__animal:
                print(f"{a.name}: {a.species}: {a.category}")

            else:
                 print("No animals were found in this enclosure.")




#Returns an easy to read summary of the enclosure
    def __str__(self):
        resident_names = ", ".join([a.name for a in self.__animal]) if self.__animal else "None"
        return(f"\nEnclosure: {self.__name}\n Size:{self.__size}\n Environment: {self.__environment}\n Animal Type: {self.__animal_type}\n Cleanliness{self.__clean}\n Current Residents: {len(self.__animal)}\n Resident Name: {resident_names}")
# Properties for encapsulated access to enclosure name, size, environment, animal type, cleanliness, and animals
    name = property(__get_name, __set_name)
    size = property(__get_size, __set_size)
    environment = property (__get_environment)
    animal_type = property(__get_animal_type)
    cleanliness = property(__get_cleanliness, __set_cleanliness)
    animals = property(__get_animals)
