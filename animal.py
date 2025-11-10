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
        self.__date = date.today()
        self.__description = description
        self.__severity = severity
        self.__treatment_notes = treatment_notes
    def __str__(self):
        return f"{self.__date} - {self.__description} -(Severity: {self.__severity})"

class Animal:
   def __init__(self, name, species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_records = []

