"""
Dividing up modules into separate files and in own directories:


# Directory File Contents:

# __init__.py
# main.py
# greetings/
#     __init__.py
#     aloha.py
#     adios.py

# __init__.py
# just an empty init file in the main directory

# main.py:
from greetings import say_hi, say_goodbye

say_hi()
say_goodbye()


# greetings/__init__.py:

from .adios import say_goodbye
from .aloha import say_hi


# greetings/adios.py:

def say_hi():
    print('hello')
    

# greetings/adios.py:

def say_goodbye():
    print('good bye')


"""
