'''
File: staff.py
Description: A brief description of this Python module.
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''''
class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff = []

    def get_name(self):
        return self.__name
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "Default Zoo"
            print(f"Invalid Name given: {self.__name} has been assigned)")

    def __get_animals(self):
        return list(self.__animals)
    def __get_enclosures(self):
        return list(self.__enclosures)
    def __get_staff(self):
        return list(self.__staff)

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

    def list_animals(self):
        print(f"Animals in Zoo: {self.__name}")
        if not self.__animals:
            print("No animals in Zoo")
        else:
            for animal in self.__animals:
                print(f"Name: {animal.name}, Type: {animal.type} Category: {animal.category}")

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

    name = property(get_name, set_name)
    animals = property(__get_animals)
    enclosures = property(__get_enclosures)
    staff = property(__get_staff)