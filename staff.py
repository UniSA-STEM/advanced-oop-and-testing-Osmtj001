'''
File: staff.py
Description: Staff module will initialise staff, and will allow them to perform tasks specific to their role. Tasks such as cleaning an enclosure, treating an animal,
feeding an animal will be run from here. Staff can also be assigned to specific enclosures and animals. 
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''''

#Staff class will take an input of Name & Role, then validate the inputs are strings before assigning. Default values are assigned & an error given for incorrect input
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.__enclosures = []
        self.__animals = []
#Getter and setter for Get Name and Get Role. These use private attributes so values are encapsulated and type-checked before being stored.
    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "Unknown Staff Member"
            print(f"Invalid Name provided. Default Name Set: {self.name}")



    def __get_role(self):
        return self.__role

    def __set_role(self, role):
        if isinstance(role, str):
            self.__role = role
        else:
            self.__role = "Unassigned"
            print(f"Invalid Role provided. Default Role Set: {self.role}")


    def __get_enclosures(self):
        return list(self.__enclosures)

    def __get_animals(self):
        return list(self.__animals)
# Assign enclosures and animals to this staff member. Each enclosure/animal is only added once; repeated assignments are ignored.
    def assign_enclosure(self, enclosure):
        if enclosure not in self.__enclosures:
            self.__enclosures.append(enclosure)
            print(f"Enclosure: {enclosure.name} is assigned to {self.name}")

    def assign_animal(self, animal):
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"Animal: {animal.name} is assigned to {self.name}")
#Returns a string function displaying the Name, role, enclosure, and animals for each staff
    def __str__(self):
        return f"Staff: {self.name}, Role: {self.role}, Enclosures: {self.__enclosures}, Animals: {self.__animals}"

# Properties for encapsulated access to name, role, and assigned animals/enclosures.
    name = property(__get_name, __set_name)
    role = property(__get_role, __set_role)
    assigned_enclosure = property(__get_enclosures)
    assigned_animal = property(__get_animals)

# Zookeeper is a specialised Staff member with role fixed to "Zookeeper". This Zookeeper will only perform tasks for animals & enclosures that are assigned to them
class Zookeeper(Staff):
    def __init__(self, name):
        Staff.__init__(self, name, "Zookeeper")

    def feed_animal(self, animal):
        if animal not in self.assigned_animal:
            print(f"Error, Animal: {animal.name} is not assigned to {self.name}")
        else:
            print(f"{self.name} is feeding {animal.name}...")
            animal.eat_food()

    def clean_enclosure(self, enclosure):
        if enclosure not in self.assigned_enclosure:
            print(f"Error, Enclosure: {enclosure} is not assigned to {self.name}")
        else:
            print(f"{self.name} is cleaning {enclosure}")
            enclosure.cleanliness = 100
            print(f"{enclosure} is now cleaned and is {enclosure.cleanliness}/100")

# Vet is a specialised Staff member with role fixed to "Vet" This Vet will only perform tasks for animals & enclosures that are assigned to them
class Vet(Staff):
    def __init__(self, name):
        Staff.__init__(self, name, "Vet")

    def health_check(self, animal, health_issue):
        if animal not in self.assigned_animal:
            print(f"Error, Animal: {animal.name} is not assigned to {self.name}")
        else:
            print(f"{self.name} is conducting a health check for {animal.name} due to {health_issue}")


    def treat_animal(self, animal, treatment_plan):
        if animal not in self.assigned_animal:
            print(f"Error, Animal: {animal.name} is not assigned to {self.name}")
        else:
            print(f"{self.name} is treating {animal.name}")
            print(f"Treatment Plan: {treatment_plan}")
