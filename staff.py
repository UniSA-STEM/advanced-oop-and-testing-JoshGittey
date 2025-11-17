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