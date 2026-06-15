# Module 13: Classes and Object-Oriented Programming

## Core Concepts

### Class Definition
```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    # Constructor — called when instance is created
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age        # Instance variable

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    # String representation
    def __str__(self):
        return f"{self.name} ({self.age})"

# Create instance
my_dog = Dog("Rex", 3)
print(my_dog.bark())       # Rex says woof!
print(my_dog)              # Rex (3)
```

### The `self` Parameter
- `self` refers to the instance calling the method
- Must be the first parameter of all instance methods
- Automatically passed by Python (you don't pass it manually)

### Instance vs Class Variables
| Type | Defined | Belongs to | Accessed via |
|------|---------|------------|--------------|
| Instance | `self.x = val` in methods | Each instance | `instance.x` |
| Class | Inside class body, outside methods | The class (shared) | `Class.x` or `instance.x` |

### Class Methods (`@classmethod`)
```python
class Employee:
    raise_amount = 1.04

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, float(salary))
```
- First parameter is `cls` (the class)
- Used for factory methods and class-level operations

### Static Methods (`@staticmethod`)
```python
class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
```
- No `self` or `cls` parameter
- Behaves like a regular function, grouped with the class for organization

### Property Decorator (`@property`)
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```
- Control attribute access with getter/setter logic
- Computed properties (like `area`) don't need a setter

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        return f"{self.name} says meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
```

### `super()`
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # Call parent's __init__
        self.age = age
```

### Method Overriding
Child classes can redefine methods from the parent class. Use `super()` to call the parent version when needed.

### Encapsulation
| Convention | Meaning | Example |
|------------|---------|---------|
| `self.x` | Public | Accessible anywhere |
| `self._x` | Protected (convention) | "Please don't touch" |
| `self.__x` | Name mangled | `_ClassName__x` (avoid subclass conflicts) |

### Magic (Dunder) Methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title          # For users (print())

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"  # For devs (repr())

    def __len__(self):
        return self.pages          # len(book)

    def __eq__(self, other):
        return self.title == other.title  # book1 == book2

    def __lt__(self, other):
        return self.pages < other.pages   # book1 < book2 (sorting)
```

### Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Auto-generated: __init__, __repr__, __eq__, __hash__
p = Point(3.0, 4.0)
print(p)              # Point(x=3.0, y=4.0)
print(p == Point(3.0, 4.0))  # True
```

### Abstract Base Classes (Brief)
```python
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def predict(self, input_data):
        pass

class LLMModel(Model):
    def predict(self, prompt):
        return f"Generated response for: {prompt}"
```

## JavaScript Comparison

| JavaScript | Python |
|------------|--------|
| `class Dog { constructor(name) {} }` | `class Dog: def __init__(self, name)` |
| `this.name` | `self.name` |
| `static method() {}` | `@staticmethod` / `@classmethod` |
| `extends` | `(ParentClass)` in class definition |
| `super()` | `super().__init__()` |
| `get name() {}` / `set name(v) {}` | `@property` / `@name.setter` |
| `toString()` | `__str__` / `__repr__` |
| Getters/setters on prototype | `@property` decorator |
| No built-in dataclasses | `@dataclass` |

## AI Relevance
- **Model classes**: Wrapper classes for LLMs (OpenAI, Anthropic, etc.)
- **Agent classes**: Autonomous AI agents with state and behavior
- **Embedding services**: Classes for text embedding and vector operations
- **RAG pipelines**: Composable pipeline classes for retrieval-augmented generation
- **Data models**: Structured output parsing with Pydantic/dataclasses
- **Service classes**: API wrappers, caching layers, rate limiters
