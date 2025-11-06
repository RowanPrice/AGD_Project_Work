# OOP exercises

class Dog:

    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


rufus = Dog('Rufus',67)
fido = Dog('Fido',41)