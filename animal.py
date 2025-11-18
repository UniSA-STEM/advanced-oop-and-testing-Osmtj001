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

    def add_animal(self):
        A_name = input("Please enter animal Name")
        A_Species = input("Please enter animal Species")
        A_Age = input("Please enter animal Age")
        A_Diet = input("Please enter animal Diet")
        A_Category = ""
        while A_Category not in Animal.Categories:
            A_Category = input(f"Please enter animal Category from {Animal.Categories}")
        A_Sound = input("Please enter animal Sound")

        return Animal(A_name, A_Species, A_Age, A_Diet, A_Category, A_Sound)

    def make_sound(self):
        print(self.sound)

    def eat_food(self):
        print(self.diet)

    def sleep(self):
        print(f"{self.name} is now sleeping. ZZZzzz.")

dummy = Animal("", "", 0, "", "", "")
new_animal = dummy.add_animal()

print(new_animal.name)
new_animal.make_sound()
# Parrot = Animal("Parrot", "bird", 12, "worms", "bird", "Cacaw")
# Parrot.make_sound()
# Parrot.sleep()
# Parrot.eat_food()
