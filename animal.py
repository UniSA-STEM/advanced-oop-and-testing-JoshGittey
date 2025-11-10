"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from datetime import date
class HealthRecord:
    def __init__ (self, description, severity, treatment_notes =" "):
        self.date = date.today()
        self.description = description
        self.severity = severity
        self.treatment_notes = treatment_notes

    def __str__(self):
        return f"{self.date} - {self.description} -(Severity: {self.severity})"

class Animal:

    def __init__(self, name, species, age, diet):
       #Encapsulated attributes
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_records = [] # list will hold HealthRecord objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    # Animal behaviours
    def make_sound(self):
        pass

    def eat(self):
        return f"{self.__name} is eating {self.__diet}"

    def sleep(self):
        return f"{self.__name} is currently sleeping"


