"""
Module 13: Classes and OOP - Exercises
35 exercises total: Easy(10), Medium(10), Hard(10), Expert(5)
Solutions at the bottom.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ============================================================
# EASY (1-10)
# ============================================================

# 1. Create a Person class with name and age
def exercise_1():
    pass


# 2. Add an introduce() method to Person
def exercise_2():
    pass


# 3. Create a Rectangle class with width and height, and area() method
def exercise_3():
    pass


# 4. Add __str__ to Rectangle to show "Rectangle(3x4)"
def exercise_4():
    pass


# 5. Create a Counter class that counts how many instances were created
def exercise_5():
    pass


# 6. Add a class method to Rectangle that creates a square
def exercise_6():
    pass


# 7. Add a static method to validate positive numbers
def exercise_7():
    pass


# 8. Create a Book class with title, author, and ISBN
def exercise_8():
    pass


# 9. Create a Library class that can hold multiple books
def exercise_9():
    pass


# 10. Add __len__ to Library to return book count
def exercise_10():
    pass


# ============================================================
# MEDIUM (11-20)
# ============================================================

# 11. Create a BankAccount class with deposit/withdraw and balance property
def exercise_11():
    pass


# 12. Create a SavingsAccount that inherits from BankAccount with interest
def exercise_12():
    pass


# 13. Create a User class with email validation via property setter
def exercise_13():
    pass


# 14. Create a Task class with status (pending/done) and toggle method
def exercise_14():
    pass


# 15. Create a TodoList class that manages Task objects
def exercise_15():
    pass


# 16. Add __lt__ to Task so they sort by creation date
def exercise_16():
    pass


# 17. Create a @dataclass for Product with name, price, quantity
def exercise_17():
    pass


# 18. Create a ShoppingCart that can add/remove products
def exercise_18():
    pass


# 19. Add @property for cart total
def exercise_19():
    pass


# 20. Create a Student class with grades list and average grade property
def exercise_20():
    pass


# ============================================================
# HARD (21-30)
# ============================================================

# 21. Create an abstract Shape class with area() and perimeter()
def exercise_21():
    pass


# 22. Implement Circle and Rectangle that inherit from Shape
def exercise_22():
    pass


# 23. Create a Logger class with singleton pattern
def exercise_23():
    pass


# 24. Create an EventEmitter class with on/off/emit methods
def exercise_24():
    pass


# 25. Create a Timeout class using context manager (__enter__/__exit__)
def exercise_25():
    pass


# 26. Create a Observable class for property change notifications
def exercise_26():
    pass


# 27. Create a class hierarchy: Animal > Mammal > Dog/Cat
def exercise_27():
    pass


# 28. Create a Composition example: Car has Engine, Wheels, Doors
def exercise_28():
    pass


# 29. Create a Comparable mixin using __gt__, __ge__, etc.
def exercise_29():
    pass


# 30. Create an Iterator class that iterates over a range with step
def exercise_30():
    pass


# ============================================================
# EXPERT (31-35)
# ============================================================

# 31. Build a minimal ORM-like class that maps to dict storage
def exercise_31():
    pass


# 32. Create a Dependency Injection container
def exercise_32():
    pass


# 33. Build a class-based finite state machine
def exercise_33():
    pass


# 34. Implement a proxy class that logs all attribute access
def exercise_34():
    pass


# 35. Create a plugin system using abstract base classes and registration
def exercise_35():
    pass


# ============================================================
# SOLUTIONS
# ============================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Rectangle2:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


class Rectangle3:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side):
        return cls(side, side)


class Rectangle4:
    @staticmethod
    def is_positive(value):
        return value > 0


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


class Library2:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


class User:
    def __init__(self, name):
        self.name = name
        self._email = ""

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value


class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.created_at = __import__('datetime').datetime.now()

    def toggle(self):
        self.done = not self.done


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task):
        self.tasks.remove(task)


class Task2:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.created_at = __import__('datetime').datetime.now()

    def __lt__(self, other):
        return self.created_at < other.created_at


from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)


class ShoppingCart2:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)

    @property
    def total(self):
        return sum(p.price * p.quantity for p in self.products)


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, msg):
        self.logs.append(msg)


class EventEmitter:
    def __init__(self):
        self._handlers = {}

    def on(self, event, handler):
        if event not in self._handlers:
            self._handlers[event] = []
        self._handlers[event].append(handler)

    def off(self, event, handler):
        if event in self._handlers:
            self._handlers[event].remove(handler)

    def emit(self, event, *args, **kwargs):
        for handler in self._handlers.get(event, []):
            handler(*args, **kwargs)


import time


class Timeout:
    def __init__(self, seconds):
        self.seconds = seconds

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        elapsed = time.time() - self.start
        if elapsed > self.seconds:
            raise TimeoutError(f"Operation timed out after {self.seconds}s")


class Observable:
    def __init__(self):
        self._observers = {}

    def watch(self, attr, callback):
        if attr not in self._observers:
            self._observers[attr] = []
        self._observers[attr].append(callback)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            old = getattr(self, name, None)
            super().__setattr__(name, value)
            for cb in self._observers.get(name, []):
                cb(name, old, value)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color


class Dog(Mammal):
    def speak(self):
        return "Woof!"


class Cat(Mammal):
    def speak(self):
        return "Meow!"


class Engine:
    def start(self):
        return "Engine running"


class Wheel:
    def rotate(self):
        return "Wheel spinning"


class Door:
    def open(self):
        return "Door opened"


class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
        self.doors = [Door() for _ in range(4)]

    def drive(self):
        return f"{self.engine.start()} - {self.wheels[0].rotate()}"


class ComparableMixin:
    def __gt__(self, other):
        return self.__lt__(other) is False and self.__eq__(other) is False

    def __ge__(self, other):
        return self.__lt__(other) is False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class RangeIterator:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += self.step
        return val


class Model:
    _registry = {}

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def save(self):
        cls = self.__class__
        if cls.__name__ not in Model._registry:
            Model._registry[cls.__name__] = []
        Model._registry[cls.__name__].append(self)

    @classmethod
    def all(cls):
        return Model._registry.get(cls.__name__, [])

    @classmethod
    def filter(cls, **kwargs):
        results = cls.all()
        for key, val in kwargs.items():
            results = [r for r in results if getattr(r, key, None) == val]
        return results


class DIContainer:
    def __init__(self):
        self._services = {}

    def register(self, name, instance):
        self._services[name] = instance

    def resolve(self, name):
        if name not in self._services:
            raise KeyError(f"Service '{name}' not registered")
        return self._services[name]


class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state
        self._transitions = {}

    def add_transition(self, from_state, to_state, event):
        key = (from_state, event)
        self._transitions[key] = to_state

    def trigger(self, event):
        key = (self.state, event)
        if key not in self._transitions:
            raise ValueError(f"Cannot transition from {self.state} with {event}")
        self.state = self._transitions[key]


class Proxy:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        print(f"Accessing: {name}")
        return getattr(self._target, name)

    def __setattr__(self, name, value):
        if name == '_target':
            super().__setattr__(name, value)
        else:
            print(f"Setting: {name} = {value}")
            super().__setattr__(name, value)


class Plugin(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class PluginManager:
    def __init__(self):
        self._plugins = {}

    def register(self, name, plugin_cls):
        if not issubclass(plugin_cls, Plugin):
            raise TypeError(f"{plugin_cls} must inherit from Plugin")
        self._plugins[name] = plugin_cls

    def run_all(self, data):
        results = {}
        for name, cls in self._plugins.items():
            plugin = cls()
            results[name] = plugin.execute(data)
        return results
