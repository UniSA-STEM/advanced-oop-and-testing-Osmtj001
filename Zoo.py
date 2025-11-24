'''
File: staff.py
Description: This Class allows the higher functions of the Zoo such as adding animals, enclosures, and staff to take place
A string is returned to list all critical information about the zoo
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''''

# The Zoo class stores collections of animals, enclosures, and staff. It acts as the central manager for the system, allowing objects to be added, removed, and displayed. The zoo name is validated before being assigned.
class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []
#Getter and setter for Zoo name. Name is validated before being stored
    def get_name(self):
        return self.__name
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "Default Zoo"
            print(f"Invalid Name given: {self.__name} has been assigned)")
#Returns read-only lists for each protected function
    def __get_animals(self):
        return list(self.__animals)
    def __get_enclosures(self):
        return list(self.__enclosures)
    def __get_staff(self):
        return list(self.__staff)

#Checks if animal/ enclosure/ staff is already in the list, if not it is appended to the animal/ enclosure/ staff list
#Similar function for remove animal/ enclosure/ staff, a check is first performed to see if the animal/ enclosure/ staff exists
    def add_animal(self, animal):
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"Animal added to Zoo: {animal.name}")
    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"Animal removed from Zoo: {animal.name}")
        else:
            print(f"Animal {animal.name} does not exist")

    def add_enclosure(self, enclosure):
        if enclosure not in self.__enclosures:
            self.__enclosures.append(enclosure)
            print(f"Enclosure added to Zoo: {enclosure.name}")
    def remove_enclosure(self, enclosure):
        if enclosure in self.__enclosures:
            self.__enclosures.remove(enclosure)
            print(f"Enclosure removed from Zoo: {enclosure.name}")
        else:
            print(f"Enclosure {enclosure.name} does not exist")

    def add_staff(self, staff):
        if staff not in self.__staff:
            self.__staff.append(staff)
            print(f"Staff added to Zoo: {staff.name}")
    def remove_staff(self, staff):
        if staff in self.__staff:
            self.__staff.remove(staff)
            print(f"Staff removed from Zoo: {staff.name}")
        else:
            print(f"Staff {staff.name} does not exist")
#Lists each animal, enclosure, or staff that has been added to the Zoo
    def list_animals(self):
        print(f"Animals in Zoo: {self.__name}")
        if not self.__animals:
            print("No animals in Zoo")
        else:
            for animal in self.__animals:
                print(f"Name: {animal.name}, Type: {animal.species} Category: {animal.category}")

    def list_enclosures(self):
        print(f"Enclosures in Zoo: {self.__name}")
        if not self.__enclosures:
            print("No enclosures in Zoo")
        else:
            for enclosure in self.__enclosures:
                print(f"Name: {enclosure.name}, Environment: {enclosure.environment}, Animal Type: {enclosure.animal_type}")

    def list_staff(self):
        print(f"Staff in Zoo: {self.__name}")
        if not self.__staff:
            print("No staff in Zoo")
        else:
            for staff in self.__staff:
                print(f"Name: {staff.name}, Role: {staff.role}")

    def __str__(self):
        return(f"Zoo: {self.name}"
               f"\n Total Animals: {len(self.__animals)}"
               f"\n Total Enclosures: {len(self.__enclosures)}"
               f"\n Total Staff: {len(self.__staff)}")

# Properties for encapsulated access to name of the zoo, animals, enclosures, and staff
    name = property(get_name, set_name)
    animals = property(__get_animals)
    enclosures = property(__get_enclosures)
    staff = property(__get_staff)
