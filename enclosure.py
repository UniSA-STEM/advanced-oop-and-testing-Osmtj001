''''
File: enclosure.py
Description: A brief description of this Python module.
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, size, environment, animal_type):
        self.__name = name
        self.__size = size
        self.__environment = environment
        self.__animal_type = animal_type
        self.__clean = 100
        self.__animal = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str) and name is not None:
            self.__name = name
            print(f"Enclosure name: {name}")
        else:
            self.__name = "Default Enclosure"
            print(f"Enclosure name did not meet requirements: {self.__name} has been assigned")
    name = property(get_name, set_name)

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if isinstance(size, int) and size is not None:
            self.__size = size
            print(f"Enclosure size: {size}")
        else:
            self.__size = "0"
            print(f"Enclosure size did not meet requirements. Size has been defaulted to {self.__size}")

    size = property(get_size, set_size)

# Enclosures are used to house animals and must include proper�es such as size,
# environmental type (e.g., aqua�c, savannah), and cleanliness level. Each enclosure is
# restricted to a single type of animal, meaning incompa�ble species should not be housed
# together (e.g., koalas should not be placed in a penguin enclosure). Enclosures should be
# able to report their current status and list the animals they contain. Your system should
# ensure that animals are only placed in enclosures that are appropriate for their species and
# environmental needs.
