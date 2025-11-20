"""
File: animal.py
Description: This module holds the code for my animal class for this project.
Author: Wieu Kuach
ID: 110409436
Username: kuawy004
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

    def __init__(self, name, species, age, diet, sound):
       #Encapsulated attributes
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__sound = sound
        self.__health_records = [] # list will hold HealthRecord objects

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_diet(self):
        return self.__diet

    def get_sound(self):
        return self.__sound

    def get_health_records(self):
        return self.__health_records

    # Properties
    name = property(get_name)
    species = property(get_species)
    age = property(get_age)
    diet = property(get_diet)
    sound = property(get_sound)
    health_records = property(get_health_records)

    # Animal behaviours
    def make_sound(self):
        return f"{self.__name} is making a {self.__sound} noise"

    def eat(self):
        return f"{self.__name} is a {self.__diet}"

    def sleep(self):
        return f"{self.__name} is currently sleeping"

    # HealthRecord Management
    def add_health_record(self, description, severity, treatment_notes = ""):
        record = HealthRecord(description, severity, treatment_notes)
        self.__health_records.append(record)

    def show_health_records(self):
        if not self.__health_records:
            return f"no health records available for {self.__name}"
        return "\n".join(str(record) for record in self.__health_records)

    def __str__(self):
        return f"{self.__name} the {self.__species}, Age: {self.__age}, Diet: {self.__diet}"




