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
        self.date = date.today
        self.description = description
        self.severity = severity
        self.treatment_notes = treatment_notes
