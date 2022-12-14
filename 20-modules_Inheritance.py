class Animal():
    def __init__(self, name: str, age: int):
        """Create a new Animal"""
        self.name = name
        self.age = age


class Cat(Animal):
    isIndoor = True

    def __init__(self, name: str, age: str, isIndoor=True):
        """Create a new cat"""
        self.isIndoor = isIndoor
        super().__init__(name, age)

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')


class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str, weight: int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')


class Frog(Animal):

    def __init__(self, name: str, age: int, color: str = "green"):
        """Create a new frog"""
        self.color = color
        super().__init__(name, age, )


if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    wiskers.speak()
    paws.speak()
    kermit = Frog('Kermit', 1, "blue")
    print(f"name: {kermit.name}, age: {kermit.age}, color: {kermit.color}")
