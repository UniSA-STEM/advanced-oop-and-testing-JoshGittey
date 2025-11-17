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
        self._name = name
        self._age = age
        self._role = role
        self._assigned_enclosures = []
        self._assigned_animals = []

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def role(self):
        return self._role


    def assign_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Assigned object must be an Enclosure")
        self._assigned_enclosures.append(enclosure)

    def unassign_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Assigned object must be an Enclosure")
        self._assigned_enclosures.remove(enclosure)

    def assign_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Assigned object must be an Animal")
        self._assigned_animals.append(animal)

    def unassign_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Assigned object must be an Animal")
        self._assigned_animals.remove(animal)

    def list_assignments(self):
        enclosure_list = ", ".join([e.biome for e in self._assigned_enclosures]) or "None"
        animal_list = ", ".join([a.name for a in self._assigned_animals]) or "None"
        return f"{self._name}'s Assignments: \n- Enclosures: {enclosure_list}\n- Animals: {animal_list}"

    def perform_duties(self):
        return f"{self._name} is currently performing staff duties" #polymorphism expected to override this

    def __str__(self):
        return f"{self._name} (Age: {self._age}), Role: {self._role}"

class Zookeeper(Staff):
    def __init__(self, name, age):
        super().__init__(name, age, "Zookeeper")

    def feed_animals(self):
        if not self._assigned_animals:
            return f"{self.name} has no animals"

        actions = [
            f"{self.name} feeds {animal.name} the {animal.species}."
            for animal in self._assigned_animals
        ]
        return "\n".join(actions)

    def clean_enclosures(self):
        if not self._assigned_enclosures:
            return f"{self.name} has no enclosures."

        actions = []
        for enclosure in self._assigned_enclosures:
            actions.append(enclosure.clean_enclosures())

        return "\n".join(actions)

    def perform_duties(self):
        return self.feed_animals() + "\n" + self.clean_enclosures()

class Veterinarian(Staff):
    def __init__(self, name, age):
        super().__init__(name, age, "Veterinarian")

    def health_check(self):
        if not self._assigned_animals:
            return f"{self.name} has no animals"
        actions = [
            f"{self.name} conducts a health check on {animal.name} the {animal.species}."
            for animal in self._assigned_animals
        ]
        return "\n".join(actions)

    def perform_duties(self):
        return self.health_check()
