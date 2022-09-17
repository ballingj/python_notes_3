"""
pip install mypy
then check if type hint is followed with command
mypy file_name.py

Add a type hint for a variable by simply adding a colon and \"
    the expected type, as in name: str, age: int. Here's what that \"
    looks like in context:
"""


class Cat():

    def __init__(self, name: str, age: int):
        if (type(name) is not str):
            raise Exception('Name must be a string')

        if(age < 0):
            raise Exception('Age must be greater than 0')
        self.name = name
        self.age = age

    def speak(self) -> None:
        print(f'{self.name} says, "purrrrrr"')


try:
    herbert = Cat('herbert', 1)
    # herbert = Cat(1, 'herbert') # errors
    herbert.speak()
except:
    print('Bad Cat')
