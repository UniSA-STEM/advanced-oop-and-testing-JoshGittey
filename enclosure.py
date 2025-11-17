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
    def __init__(self, size, biome, max_capacity):
        self.__size = size
        self.__biome = biome
        self.__animals = []
        self.__max_capacity = max_capacity

    def add_animal(self, animal):
      if not isinstance(animal, Animal):
          raise TypeError("Animal must be an object to be added")

      if animal in self.__animals:
          raise ValueError("Animal in enclosure already")

      if self.check_animal_capacity():
          self.__animals.append(animal)
          return f"{animal.name} has been added to the enclosure"
      else:
          return f"Enclosure is full, {animal.name} can not be added"

    def check_animal_capacity(self):
        return len(self.__animals) < self.__max_capacity

    def remove_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Animal must be an object to be removed")
        self.__animals.remove(animal)

    def list_animals(self):
        if not self.__animals:
            return f"No animals are in this enclosure ({self.__biome})"
        return "\n".join(f"{animal.name} the ({animal.species}), Age: {animal.age} years old" for animal in self.__animals)





