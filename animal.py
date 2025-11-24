''''
File: animal.py
Description: This module allows the Animal class to be instantiated. This class allows for values name, species, age, diet, category, sound & health issues
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
#Allows for global use of the Category within the Zoo. These are validated before being accepted
    Categories = ["Mammal", "Bird", "Reptile", "Fish", "Amphibian", "Insect"]
#Basic attributes for all animals. Validation is used to ensure the correct data is accepted
    def __init__(self, name, species, age, diet, category, sound):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.category = category
        self.sound = sound
        self.__health_issues = []

#Animal makes its sound
    def make_sound(self):
        print(f"{self.name} sounding: {self.sound}")
#Animal eats its food
    def eat_food(self):
        print(f"{self.name} is eating {self.diet}")
#Animal goes to sleep
    def sleep(self):
        print(f"{self.name} is now sleeping. ZZZzzz.")
#Getter & Setter for animal category. Ensures data is valid, otherwise the default value of "Mammal" is given
    def __get_category(self):
        return self.__category

    def __set_category(self, category):
        if category in Animal.Categories:
            self.__category = category
        else:
            print(f"Invalid category: '{category}'. Defaulting to 'Mammal'.")
            self.__category = "Mammal"
#Adds a health issue to the animal
    def add_health_issue(self, health_issue):
        self.__health_issues.append(health_issue)
        print(f"{self.name}: Health Issue: {health_issue}")
#Checks if the health issue exists. If it does, it is marked as "Resolved"
    def resolve_health_issues(self, health_issues):
        if health_issues in self.__health_issues:
            health_issues.close_issue()
            print(f"{self.name}: Health Issue: {health_issues} has now been resolved")
        else:
            print(f"Error ~~ Health Issue: {health_issues} not found for {self.name}")
#Returns a list of all active health issues
    def get_active_issues(self):
        return [issue for issue in self.__health_issues if issue.active]
#Returns all health issues
    def get_all_issues(self):
        return list(self.__health_issues)
#Returns True or False if a health issue is active. Is used for when trying to move an animal into an enclosure as an error is given if health issue is active
    def has_active_issues(self):
        return any(issue.active for issue in self.__health_issues)
#Prints health report for animal
    def print_report(self):
        print(f"Health Report for {self.name}:")
        if not self.__health_issues:
            print(f"No health issues found for {self.name}")
        else:
            for issue in self.__health_issues:
                print(f"Health Issue: {issue}")
#Property for category which allows for encapsulated access
    category = property(__get_category, __set_category)
#Str function to easily display animal data to user
#Active issues & total issues are displayed after returning the len of each ones list
    def __str__(self):
        active_issues = len(self.get_active_issues())
        total_issues = len(self.get_all_issues())
        return (f"Animal: {self.name}"
                f"\n Species: {self.species}"
                f"\n Age: {self.age}"
                f"\n Diet: {self.diet}"
                f"\n Category: {self.category}"
                f"\n Sound: {self.sound}"
                f"\n Health Issues: {total_issues} total, {active_issues} active")
