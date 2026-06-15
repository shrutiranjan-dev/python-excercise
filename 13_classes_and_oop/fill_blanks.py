"""
Module 13: Classes and OOP - Fill in the Blanks
Fill in the _____ with the correct code. Answers at the bottom.
"""

# ============================================================
# Question 1
# ============================================================
# Class definition
_____ Dog:
    pass

# ============================================================
# Question 2
# ============================================================
# Constructor method
class Dog:
    def _____(self, name):
        self.name = name

# ============================================================
# Question 3
# ============================================================
# The first parameter of instance methods is always _____.

# ============================================================
# Question 4
# ============================================================
# Create an instance
my_dog = _____("Buddy", 3)

# ============================================================
# Question 5
# ============================================================
# Instance method
class Dog:
    def bark(self):
        return f"{self.name} says _____"

# ============================================================
# Question 6
# ============================================================
# Class variable
class Dog:
    _____ = "Canine"  # Shared by all instances

# ============================================================
# Question 7
# ============================================================
# Access class variable via class name
print(Dog._____)

# ============================================================
# Question 8
# ============================================================
# Class method decorator
class Employee:
    @_____
    def set_raise(cls, amount):
        cls.raise_amount = amount

# ============================================================
# Question 9
# ============================================================
# Static method decorator
class MathUtils:
    @_____
    def is_even(n):
        return n % 2 == 0

# ============================================================
# Question 10
# ============================================================
# Property decorator (getter)
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @_____
    def radius(self):
        return self._radius

# ============================================================
# Question 11
# ============================================================
# Property setter
class Circle:
    @property
    def radius(self):
        return self._radius

    @radius._____
    def radius(self, value):
        self._radius = value

# ============================================================
# Question 12
# ============================================================
# Inheritance
class Animal:
    def speak(self):
        pass

class Dog(_____):
    def speak(self):
        return "Woof!"

# ============================================================
# Question 13
# ============================================================
# Call parent's __init__ with super()
class Child(Parent):
    def __init__(self, name, age):
        _____().__init__(name)
        self.age = age

# ============================================================
# Question 14
# ============================================================
# String representation for users
class Book:
    def _____(self):
        return self.title

# ============================================================
# Question 15
# ============================================================
# String representation for developers
class Book:
    def _____(self):
        return f"Book('{self.title}')"

# ============================================================
# Question 16
# ============================================================
# Length magic method
class Team:
    def _____(self):
        return len(self.members)

# ============================================================
# Question 17
# ============================================================
# Equality magic method
class Person:
    def _____(self, other):
        return self.id == other.id

# ============================================================
# Question 18
# ============================================================
# Less-than magic method (for sorting)
class Product:
    def _____(self, other):
        return self.price < other.price

# ============================================================
# Question 19
# ============================================================
# Protected attribute convention (single underscore)
self._secret = "should not touch"

# ============================================================
# Question 20
# ============================================================
# Name mangled attribute (double underscore)
self.__private = "name will be mangled to _ClassName__private"

# ============================================================
# Question 21
# ============================================================
# Dataclass decorator
from dataclasses import dataclass

@_____
class Point:
    x: float
    y: float

# ============================================================
# Question 22
# ============================================================
# Abstract base class
from abc import ABC, _____

class Model(ABC):
    @abstractmethod
    def predict(self, data):
        pass

# ============================================================
# Question 23
# ============================================================
# Abstract method decorator
class Model(ABC):
    @_____
    def predict(self, data):
        pass

# ============================================================
# Question 24
# ============================================================
# Check if an object is an instance of a class
result = _____(my_dog, Dog)

# ============================================================
# Question 25
# ============================================================
# Check if a class is a subclass of another
result = _____(Dog, Animal)

# ============================================================
# Question 26
# ============================================================
# Type hint for self parameter (Python 3.11+)
class MyClass:
    def method(self: "_____") -> None:
        pass

# ============================================================
# Question 27
# ============================================================
# Class method that acts as an alternative constructor
class Person:
    @classmethod
    def _____(cls, csv_string):
        name, age = csv_string.split(",")
        return cls(name, int(age))

# ============================================================
# Question 28
# ============================================================
# Call parent method with super()
class Dog(Animal):
    def speak(self):
        parent_sound = _____().speak()
        return f"{parent_sound} Woof!"

# ============================================================
# ANSWERS
# ============================================================
"""
1. class
2. __init__
3. self
4. Dog
5. woof
6. species
7. species
8. classmethod
9. staticmethod
10. property
11. setter
12. Animal
13. super
14. __str__
15. __repr__
16. __len__
17. __eq__
18. __lt__
19. (no blank - convention reference)
20. (no blank - convention reference)
21. dataclass
22. abstractmethod
23. abstractmethod
24. isinstance
25. issubclass
26. MyClass
27. from_string
28. super
"""
