'''
# The final directory tree should appear as the following:

|____ __init__.py
|____ pets.py
|____ animals/
| | ____ __init__.py
| | ____ cat.py
| | ____ animal.py
| | ____ frog.py
| | ____ dog.py


# animals/__init__.py

from .frog import Frog
from .cat import Cat
from .dog import Dog


# animals/animal.py

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name: str, age: int):
        """Create a new cat"""
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass


# animals/cat.py

from .animal import Animal

class Cat(Animal):
    isIndoor = True

    def __init__(self, name: str, age: int, isIndoor=True):
        """Create a new cat"""
        self.isIndoor = isIndoor
        super().__init__(name, age)

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')

# animals/dog.py

from .animal import Animal

class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str, weight: int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')


# animals/frog.py

from .animal import Animal

class Frog(Animal):

    def __init__(self, name: str, age: int, color='Green'):
        self.color = color
        super().__init__(name, age)

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "ribbit"')


# pet.py

from animals import Cat, Dog, Frog

if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    wiskers.speak()
    paws.speak()
    kermit = Frog('Kermit', 1, "blue")
    print(f"name: {kermit.name}, age: {kermit.age}, color: {kermit.color}")


'''
