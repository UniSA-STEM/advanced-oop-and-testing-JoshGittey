"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from enclosure import Enclosure

class Staff:
    def __init__(self, name, age, role):
        self.__name = name
        self.__age = age
        self.__role = role
        self.__assigned_enclosures = []
        self.__assigned_enclosures = []

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def role(self):
        return self.__role


    def assign_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Assigned object must be an Enclosure")
        self.__assigned_enclosures.append(enclosure)

    def unassign_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Assigned object must be an Enclosure")
        self.__assigned_enclosures.remove(enclosure)

    def assign_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Assigned object must be an Animal")
        self.__assigned_enclosures.append(animal)

    def list_assignments(self):
        enclosure_list = ", ".join([e.biome for e in self.__assigned_enclosures]) or "None"
        animal_list = ", ".join([a.name for a in self.__assigned_animals]) or "None"

        return f"{self.__name}'s Assignments: \n- Enclosures: {enclosure_list}\n- Animals: {animal_list}"

    def perform_duties(self):
        return f"{self.__name} is currently performing staff duties" #polymorphism expected to override this

    def __str__(self):
        return f"{self.__name} (Age: {self.__age}), Role: {self.__role}"

class Zookeeper(Staff):
    def __init__(self, name, age):
        super().__init__(name, age, "Zookeeper")

    def feed_animals(self):
