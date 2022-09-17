"""
Instructions

In this exercise, you'll create a memoize decorator that can be used to cache the result of any pure function – a function whose output is purely a result of its input.

Concretely, you'll fill out the body of the following memoize decorator:

import functools


def memoize(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

Currently, this decorator doesn't do anything special – it just builds a wrapper function and forwards arguments and return values to and from the captured function.

You'll have to edit this decorator so that it caches the result of calling the decorated function. For example, imagine that we write

@memoize
def long_operation(x, y):
    time.sleep(5)   # Or some other suitable long expression.
    return x + y

The first time we call long_operation(3, 7), we'll need to execute the entire function body, however long it might take. However, any subsequent calls to the decorated long_operation(3, 7) should return immediately, because our decorator will have cached the information that the arguments (3, 7) result in the value 10. The first call to long_operation(5, 12) would still have to go through the function body.

As another example, consider the function

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

If we try to call fib(5), we'll need to evaluate fib(4) and fib(3). To evaluate fib(4) and fib(3), we'll need to evaluate fib(3) and fib(2) and fib(2) and fib(1). To evaluate fib(3) and fib(2) and fib(2) and fib(1), we'll need to evaluate fib(2) and fib(1) and fib(1) and fib(0) and fib(1) and fib(0) and fib(1). There's a lot of redundant work. If we instead remember the value of, perhaps, fib(3) after we compute it, we'll only need to compute a few values. This is the great power of caching.
What to do

You'll modify it in the following ways:

Add a ._cache attribute on the captured function, as a mapping from the function's arguments to the function's return values.

In the body of the wrapper function, create a key that uniquely represents the supplied arguments. One possible option is (args, tuple(kwargs.items()))

Then, if you've seen the key (collection of arguments) before, you shouldn't run the captured function, and should just return the cached value. Otherwise, you'll have to run the captured function – but make sure to save the value in the cache so that future calls will be faster!
Why?

Memoization, or caching, is an incredibly important feature of any highly-performant system. By avoiding unnecessary function calls, you can sometimes find surprising speed-ups in algorithms. Memoization can also change the asymptotic runtime behavior of certain functions (especially recursive ones).
Note

This is actually already implemented in the language, as functools.cache (or for Python 3.2+, functools.lru_cache), which has even additional features like the ability to track cache hits and misses! Python really does have it all.

"""

import functools

""" my solution 

def memoize(function):
    _cache = {}   # will store the snapshot of passed argument and the returned value

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in _cache:
            return _cache[key]
        else:
            _cache[key] = function(*args, **kwargs)
            return _cache[key]
    return wrapper

"""
# official solution

def memoize(function):
    function._cache = {}

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args, **kwargs)
        return function._cache[key]
    return wrapper


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(10))
    print(fib(25))
    print(fib(40))
    # print(fib(50))
    # print(fib(100))
    # print(fib(110))

""" expected output
55
75025
12586269025
354224848179261915075
43566776258854844738105
"""
