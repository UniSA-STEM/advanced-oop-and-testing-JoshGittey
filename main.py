"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from enclosure import Enclosure
from staff import Staff
from animal import Animal

# animals created
Simba = Animal(name = "Leo", species= "Lion", age =5, diet= "Carnivore", sound= "Roar")
Ella = Animal("Ella", "Elephant", 10, "Herbivore", "trumpet")
Mona = Animal("Mona", "Monkey", 3, "Omnivore", "screech")

Simba.add_health_record("Checkup", "Low", "All good")
Ella.add_health_record("Trunk injury", "Medium", "Bandaged")

# Create enclosures
savannah = Enclosure(1000, "Savannah", 80, 3, allowed_species=["Lion"])
savannah2 = Enclosure(1000, "Savannah", 80, 3, allowed_species=["Elephant"])
jungle = Enclosure(500, "Jungle", 90, 5, allowed_species=["Monkey"])
