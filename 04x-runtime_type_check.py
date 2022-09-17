"""
You'll need to support three levels of severity. When the severity is zero, you should perform no error checking at all. In 
this case, your decorator can be a no-op decorator that just forwards the captured function through. When the severity is 1, 
you should print an error message describing the violation. When the severity is 2, you should raise an error with the violation. 
To raise a TypeError with a message, use raise TypeError(msg).

You can design this in any way you see fit. We recommend following this pattern:

define check_types
    if the severity is zero, return a no-op decorator
    define a generic messaging function that prints a message if the severity is 1 and raises a TypeError if the severity is 2
    define checker, which will itself be a decorator!
        look at the function's `__annotations__` - if there aren't any, forward the function through!
            make sure that each of the function's annotations is a type (e.g. int) and not some other value (e.g. 5)
        define a wrapper function, itself decorated with `functools.wraps`, which takes in *args and **kwargs
            bind the arguments *args and **kwargs to the original function, to see what _would_ go into the function
            check that each of the arguments match the expected type in the annotations dictionary, if its present
                if any fail, send a message that there was a violation
            compute the function's actual return value on the supplied arguments
            check that the return value matches the expected type of the return value in the annotations dictionary, if present
                if it fails, send a message that there was a violation
            return the return value
        return the wrapper function
    return the checker decorator

"""

import functools
import inspect


# bind_args(function, *args, **kwargs) that returns a mapping from parameter names to
#  their bound values, when the function is called with the captured arguments.
def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments


def check_types(severity=1):
    if severity == 0:
        # return a no-op decorator
        return lambda function: function

    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)

    def checker(function):
        expected = function.__annotations__
        
        if not expected:
            return function
        assert(all(map(lambda exp: type(exp) == type, expected.values())))
        #assert(all(map(lambda exp: isinstance(exp, type), expected.values())))

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            # do something
            bound_arguments = bind_args(function, *args, **kwargs)
            for arg, val in bound_arguments.items():
                if arg not in expected:
                    continue
                if not isinstance(val, expected[arg]):
                    message(f"Bad Argument! Received {arg}={val}, expecting object of type {expected[arg]}")

            retval = function(*args, **kwargs)
            if 'return' in expected and not isinstance(retval, expected['return']):
                message(f"Bad Return Value! {retval}, but expected value of type {expected['return']}")
            return retval
        return wrapper
    return checker

# This decorator-factory can be used to produce a decorator and immediately apply it to a function:
@check_types(severity=0)
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'


#def demonstrate_complex_arguments(a, b=1, *c, d=1, **e):
#    pass

#print(dict(bind_args(demonstrate_complex_arguments, 1, 2, 3, 4, d=10, e=11, f=12, g=13)))
# {'a': 1, 'b': 2, 'c': (3, 4), 'd': 10, 'e': {'e': 11, 'f': 12, 'g': 13}}

# When used correctly, everything is great!
print(foo(3, 'ABCDE'))  # => False
print(foo(1, 'WXYZ'))

# But if the arguments are the wrong type, this decorator function will severely complain!
# print(foo('WXYZ', 1))
# Lots of information about an error
# TypeError: Bad Argument! Received a=WXYZ, expecting object of type <class 'int'>
