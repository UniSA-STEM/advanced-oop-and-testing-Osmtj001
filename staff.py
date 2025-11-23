'''
File: staff.py
Description: A brief description of this Python module.
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''''

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.__enclosures = []
        self.__animals = []

    def __get_name(self):
        return self.name

    def __set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "Unknown Staff Member"
            print(f"Invalid Name provided. Default Name Set: {self.name}")



    def __get_role(self):
        return self.role

    def __set_role(self, role):
        if isinstance(role, str):
            self.role = role
        else:
            self.role = "Unassigned"
            print(f"Invalid Role provided. Default Role Set: {self.role}")


    def __get_enclosures(self):
        return self.__enclosures

    def __get_animals(self):
        return self.__animals

    def assign_enclosure(self, enclosure):
        if enclosure not in self.__enclosures:
            self.__enclosures.append(enclosure)
            print(f"Enclosure: {enclosure} is assigned to {self.name}")

    def assign_animal(self, animal):
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"Animal: {animal} is assigned to {self.name}")

    def __str__(self):
        return f"Staff: {self.name}, Role: {self.role}, Enclosures: {self.__enclosures}, Animals: {self.__animals}"

    name = property(__get_name, __set_name)
    role = property(__get_role, __set_role)
    assigned_enclosure = property(__get_enclosures)
    assigned_animal = property(__get_animals)

# Staff members play a key role in zoo opera�ons and should be modeled with roles such as
# zookeeper or veterinarian, each with specific responsibili�es. Staff should be able to perform
# ac�ons including feeding animals, cleaning enclosures, and conduc�ng health checks. They
# should also be assigned to specific animals or enclosures based on their role and du�es.