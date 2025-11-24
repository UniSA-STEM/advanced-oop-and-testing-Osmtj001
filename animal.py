''''
File: animal.py
Description: This module allows the Animal class to be instantiated. This class allows for values name, species, age, diet, category, sound & health issues
The Health class is also included in the module which allows for recording health issues, current treatment, date recorded, and data validation
to ensure the correct values are passed. This links with other modules such as enclosure to ensure no animal undergoing treatment will be moved into
a different enclosure
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


#Allows user to assign medical issues to a specific animal, and resolve with a treatment plan
#Each issue is stored with a description, date reported, level of severity, and treatment plan
#A Boolean value is assigned to "Active" which is checked when attempting to resolve a health issue, or relocate an animal to an enclosure
#Active is set to true by default
class Health:
    def __init__(self, description, date_reported, level, treatment_plan):
        self.description = description
        self.date_reported = date_reported
        self.level = level
        self.treatment_plan = treatment_plan
        self.active = True

#Getter & Setter for various functions. Similar data validation is executed for each one to ensure the correct data is entered
#If the incorrect data is provided, an error is displayed and a default variable is set
    def __get_description(self):
        return self.__description
    def __set_description(self, description):
        if isinstance(description, str):
            self.__description = description
        else:
            self.__description = "Default Description"
            print(f"Invalid Description: {self.__description} has been set")

    def __get_date_reported(self):
        return self.__date_reported
#Data validation accepts a string, with the correct date format being 24-11-2025
    def __set_date_reported(self, date_reported):
        if isinstance(date_reported, str):
            self.__date_reported = date_reported
        else:
            self.__date_reported = "Unknown"
            print(f"Invalid Date Provided: {self.__date_reported} has been set")

    def __get_level(self):
        return self.__level

    def __set_level(self, level):
        if isinstance(level, str):
            self.__level = level
        else:
            self.__level = "Unknown"
            print(f"Invalid Level of Severity Provided {self.__level} has been set")

    def __get_treatment_plan(self):
        return self.__treatment_plan
    def __set_treatment_plan(self, treatment_plan):
        if isinstance(treatment_plan, str):
            self.__treatment_plan = treatment_plan
        else:
            self.__treatment_plan = "Unknown"
            print(f"Invalid Treatment Plan: {self.__treatment_plan} has been set")
#Getter and setter for active function, ensures active can only be set as a boolean value
    def __get_active(self):
        return self.__active
    def __set_active(self, active):
        if isinstance(active, bool):
            self.__active = active
        else:
            self.__active = True
            print(f"Invalid Active Value: {self.__active} has been set for patient illness value")
#Called to set active to false, closing the issue
    def close_issue(self):
        self.active = False
#Provides a summary of the health issue
    def __str__(self):
        active_status = "Active" if self.active else "Resolved"
        return(f"Health Issue: {self.description},"
               f"Date Reported: {self.date_reported},"
               f"Level of Severity: {self.level},"
               f"Treatment Plan: {self.treatment_plan},"
               f"Active Status: {active_status}")
# Properties for encapsulated access to description, date, level, treatment & active status
#Allows for validation to occur
    description = property(__get_description, __set_description)
    date = property(__get_date_reported, __set_date_reported)
    level = property(__get_level, __set_level)
    treatment = property(__get_treatment_plan, __set_treatment_plan)
    active = property(__get_active, __set_active)
