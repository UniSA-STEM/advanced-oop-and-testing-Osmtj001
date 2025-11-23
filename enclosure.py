''''
File: enclosure.py
Description: A brief description of this Python module.
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
class Enclosure:
    def __init__(self, name, size, environment, animal_type):
        self.name = name
        self.size = size
        self.__environment = environment
        self.__animal_type = animal_type
        self.cleanliness = 100
        self.__animal = []

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

    def __get_animals(self):
        return list(self.__animal)

    def add_animal(self, animal):
        if not isinstance(animal, str) and animal.category == self.__animal_type:
            self.__animal.append(animal)
            print(f"Added animal: {animal.name} to enclosure {self.name}")
        else:
            print(f"This enclosure is for {self.__animal_type} animals only.")

    def remove_animal(self, animal):
        if not isinstance(animal, str) and animal in self.__animal:
            self.__animal.remove(animal)
            print(f"Removed animal: {animal} from Enclosure {self.name}")

    def list_animals(self):
        if len(self.__animal) > 0:
            for a in self.__animal:
                print(f"{a.name}: {a.species}: {a.category}")

            else:
                 print("No animals were found in this enclosure.")





    def __str__(self):
        resident_names = ", ".join([a.name for a in self.__animal]) if self.__animal else "None"
        return(f"\nEnclosure: {self.__name}\n Size:{self.__size}\n Environment: {self.__environment}\n Animal Type: {self.__animal_type}\n Cleanliness{self.__clean}\n Current Residents: {len(self.__animal)}\n Resident Name: {resident_names}")

    name = property(__get_name, __set_name)
    size = property(__get_size, __set_size)
    environment = property (__get_environment)
    animal_type = property(__get_animal_type)
    cleanliness = property(__get_cleanliness, __set_cleanliness)
    animals = property(__get_animals)

# penguin = Animal("Pingu","Swan", 10, "Worms", "E", "Pizaaaa")
# p1 = Animal("Swanny","Swan", 10, "Worms", "E", "Meow")
# E1=Enclosure("E1", 10, "E", "E")
# print("\n")
# E1.add_animal(penguin)
# E1.add_animal(p1)
# print(E1)

# Enclosures are used to house animals and must include proper�es such as size,
# environmental type (e.g., aqua�c, savannah), and cleanliness level. Each enclosure is
# restricted to a single type of animal, meaning incompa�ble species should not be housed
# together (e.g., koalas should not be placed in a penguin enclosure). Enclosures should be
# able to report their current status and list the animals they contain. Your system should
# ensure that animals are only placed in enclosures that are appropriate for their species and
# environmental needs.
