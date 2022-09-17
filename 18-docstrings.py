"""
Docstrings:

Docstrings are specified by the PEP 257 conventions. They are used to describe \"
    the behavior of modules, classes, and functions.

Doctest:

Doctest is a simple module that allows you to declare expected outputs for \"
specific inputs of a method directly in a docstring comment. For example: 

"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(c=1, d=2):
    """Return the quotient of a divided by b.
    Arguments:
        c {int} -- the numerator (defaults 1)
        d {int} -- the denominator (defaults 2)
    Raises:
        Exception: if b is 0
    """
    if d == 0:
       raise Exception("Cannot divide by zero.")
    return c / d


def is_healthy(food):
    """Return True if it is known to be healthy; assume unknown food is unhealthy"""
    if food == 'burger':
        return False
    elif food == 'salad':
        return True
    else:
        return False


"""Doctest"""


def add(e, f):
    """Return the sum of e and f

    >>> add(1, 1)
    2
    """
    return e+f
