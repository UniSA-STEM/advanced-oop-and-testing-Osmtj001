''''
File: animal.py
Description: A brief description of this Python module.
Author: Trent Osmond
ID: 110316757
Username: Osmtj001
This is my own work as defined by the University's Academic Integrity Policy.
'''

# The system should allow for the crea�on and management of animals, each with atributes
# such as name, species, age, and dietary needs. Animals may belong to different categories—
#  such as mammals, rep�les, or birds—which may share common behaviors while also
# exhibi�ng unique traits. All animals should be capable of performing basic ac�ons like
# making sounds, ea�ng, and sleeping.

class Animal:

    Categories = ["Bird"]
    def __init__(self, name, species, age, diet, category, sound):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.category = category
        self.sound = sound
        self.__health_issues = []


    def make_sound(self):
        print(f"{self.name} sounding: {self.sound}")

    def eat_food(self):
        print(f"{self.name} is eating {self.diet}")

    def sleep(self):
        print(f"{self.name} is now sleeping. ZZZzzz.")

    def add_health_issue(self, health_issue):
        self.__health_issues.append(health_issue)
        print(f"{self.name}: Health Issue: {health_issue}")

    def resolve_health_issues(self, health_issues):
        if health_issues in self.__health_issues:
            health_issues.close_issue()
            print(f"{self.name}: Health Issue: {health_issues} has now been resolved")
        else:
            print(f"Error ~~ Health Issue: {health_issues} not found for {self.name}")

    def get_active_issues(self):
        return [issue for issue in self.__health_issues if issue.active]

    def get_all_issues(self):
        return list(self.__health_issues)

    def has_active_issues(self):
        return any(issue.active for issue in self.__health_issues)

    def print_report(self):
        print(f"Health Report for {self.name}:")
        if not self.__health_issues:
            print(f"No health issues found for {self.name}")
        else:
            for issue in self.__health_issues:
                print(f"Health Issue: {issue}")

class Health:
    def __init__(self, description, date_reported, level, treatment_plan):
        self.description = description
        self.date_reported = date_reported
        self.level = level
        self.treatment_plan = treatment_plan
        self.active = True

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

    def __get_active(self):
        return self.__active
    def __set_active(self, active):
        if isinstance(active, bool):
            self.__active = active
        else:
            self.__active = True
            print(f"Invalid Active Value: {self.__active} has been set for patient illness value")

    def close_issue(self):
        self.active = False

    def __str__(self):
        active_status = "Active" if self.active else "Resolved"
        return(f"Health Issue: {self.description},"
               f"Date Reported: {self.date_reported},"
               f"Level of Severity: {self.level},"
               f"Treatment Plan: {self.treatment_plan},"
               f"Active Status: {active_status}")

    description = property(__get_description, __set_description)
    date = property(__get_date_reported, __set_date_reported)
    level = property(__get_level, __set_level)
    treatment = property(__get_treatment_plan, __set_treatment_plan)
    active = property(__get_active, __set_active)