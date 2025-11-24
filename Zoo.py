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
