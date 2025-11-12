"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

Simba = Animal(name = "Leo", species= "Lion", age =5, diet= "Carnivore", sound= "Roar")
Rio = Animal(name= "Rio", species= "Eagle", age= 9, diet= "Carnivore", sound= "Squawk")
Cody = Animal(name= "Cody", species= "Penguin", age= 2, diet= "Carnivore", sound= "Chirp")

print(Simba)
print(Rio)
print(Cody)

print(Simba.make_sound())
print(Rio.make_sound())
print(Cody.make_sound())

print(Simba.eat())
print(Rio.eat())
print(Cody.eat())

print(Simba.sleep())
print(Rio.sleep())
print(Cody.sleep())

Simba.add_health_record(description= "Cut on Paw", severity= "Low", treatment_notes= "Wound has been cleaned and bandage has been applied")
Cody.add_health_record(description= "Feather loss", severity= "Medium", treatment_notes= "Vitamin supplement has been applied")

print(Simba.show_health_records())
print(Rio.show_health_records())
print(Cody.show_health_records())