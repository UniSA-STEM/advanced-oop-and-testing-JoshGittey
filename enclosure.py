"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
import animal
from animal import Animal

class Enclosure:
    def __init__(self, size, biome, cleanliness_level, max_capacity, allowed_species=None):
        self.__size = size
        self.__biome = biome
        self.__cleanliness_level = cleanliness_level
        self.__animals = []
        self.__max_capacity = max_capacity
        self.__allowed_species = allowed_species if allowed_species else []

    @property
    def size(self):
        return self.__size

    @property
    def biome(self):
        return self.__biome

    @property
    def cleanliness_level(self):
        return self.__cleanliness_level

    @cleanliness_level.setter
    def cleanliness_level(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Cleanliness level must be between 0 and 100")
        self.__cleanliness_level = value

    @property
    def max_capacity(self):
        return self.__max_capacity

    def add_animal(self, animal):
      if not isinstance(animal, Animal):
          raise TypeError("Animal must be an object to be added")
      if animal in self.__animals:
          return f"{animal.name} is already in this enclosure already"
      if self.__allowed_species and animal.species not in self.__allowed_species:
          return f"{animal.species} is not allowed in this {self.__biome} enclosure"
      if not self.check_animal_capacity():
          return f"enclosure is full {animal.name} cannot be added"

      self.__animals.append(animal)
      return f"Added {animal.name} to the enclosure"

    def remove_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Animal must be an object to be removed")
        if animal not in self.__animals:
            return f"{animal.name} is not in this enclosure"

        self.__animals.remove(animal)
        return f"Removed {animal.name} from the enclosure"

    def check_animal_capacity(self):
        return len(self.__animals) <= self.__max_capacity

    def list_animals(self):
        if not self.__animals:
            return f"No animals are in this enclosure ({self.__biome})"
        return "\n".join(f"{animal.name} the ({animal.species}), Age: {animal.age} years old" for animal in self.__animals)

    def clean_enclosure(self):
        self.__cleanliness_level = 100
        return f"the {self.__biome} has been cleaned up. The cleanliness is now back to 100%"

    def __str__(self):
        return f"Enclosure ({self.__biome}) - {len(self.__animals)}/{self.__max_capacity} animals"





