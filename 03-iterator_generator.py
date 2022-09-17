# Iterator and Generator

# Iterator
# Build an iterator over [1,2,3]
it = iter([1, 2, 3])

next(it)  # => 1
next(it)  # => 2
next(it)  # => 3
# next(it)  # raises StopIteration error


it2 = iter(range(100))
66 in it2
next(it2)  # => 67

iterabel = [2, 5, 4, 9]
max(iterabel)
#9
min(iterabel)
#2
2 in (iterabel)
# True
2 in iter(iterabel)
# True
3 in (iterabel)
#False
7 in (iterabel)
#False
 

# Generator
"""
gen = (costly_fn(data) for data in iterable)
print(gen)  
# <generator object <genexpr> at 0x109055cf0>
next(gen)  
# => The first transformed element.
next(gen)  
# => The second transformed element.


"""
## Generator Expressions
[x ** 2 for x in range(10)]
# the top is a list comprehension - the data is consumed all at once
# the bottom is a generator expression -- parenthesis versus squate brackets
ex = (x ** 2 for x in range(10))
# in generator expressions, the values do not get consumed right away

# generator gets consumed in the following ways:
list(ex)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # list will consume all at once
list(ex)
# []

# one at a time
ex = (x ** 2 for x in range(10))
next(ex)
# 0
next(ex)
# 1
next(ex)
# 4
next(ex)
# 9
next(ex)
# 16
list(ex)
# [25, 36, 49, 64, 81]

# iterate over the data
ex = (x ** 2 for x in range(10))
25 in ex
# True
list(ex)
# [36, 49, 64, 81]  # elements were consumed up to the value 25


"""
A generator function looks like a normal function, except it contains the keyword yield.
When called, a generator function returns a generator iterator that can produce subsequent
values on demand by running the function until it encounters a yield statement, and then pausing.
In this way, generators are an advanced way to describe a stream of data.
To build a generator function, define a function containing the yield keyword. To use it, call the
generator function to get a generator iterator, and iterator over it to your heart's content.
"""
# Generator Function

def generate_ints(n):
    for i in range(n):
        yield i


g = generate_ints(3)  # Doesn't start the function! Just sets up the iterator
type(g)  # => <class 'generator'>

next(g)  # => 0. Run until the next yield statement.
next(g)  # => 1. Run until the next yield statement.
next(g)  # => 2. Run until the next yield statement.

# next(g)   # raises StopIteration. Finished the function before finding another yield statement.


def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


g = generate_fibs()
next(g)  # => 1
next(g)  # => 1
next(g)  # => 2
next(g)  # => 3
next(g)  # => 5
# max(g)   # Don't run this line of code. What happens?  because, it will never reach the max value

# Representations of infinite streams of data, like the generate_fibs generator function, can be nicely paired with other consumers:
def fibs_under(n):
    for fib in generate_fibs():  # Loops over 1, 1, 2, 3, 5...
        if fib > n:
            break
        print(fib)

fibs_under(21)
