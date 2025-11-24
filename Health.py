''''
File: Health.py
Description: This module instantiates the Health class & allows for recording health issues, current treatment, date recorded, and data validation
to ensure the correct values are passed. This links with other modules such as enclosure to ensure no animal undergoing treatment will be moved into
a different enclosure
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''

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
