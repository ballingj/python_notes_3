# Higher Order Functions with map and filter

"""map function
map(some_functionn, iterable)
The map function transforms a stream of data from an iterable and produces a stream of data by 
applying the function to each element. Interestingly, the first argument to map is a function object! 
This is the first time we've seen a function object be passed as an argument to another function.
"""

map(float, ['1.0', '2.5', '-4.1'])

m = map(float, ['1.0', '2.5', '-4.1'])
print(m)    # => <map object at 0x00000201972C2550>

m = list(m)
print(m)    # => [1.0, 2.5, -4.1]


"""Filter function
filter(predicate_function, iterable)
The filter function filters only the elements from a stream of data that pass through a predicate function. 
As before, the first argument to filter is a function object!
"""

def is_even(n):
    return n % 2 == 0


filter(is_even, range(50))
n = filter(is_even, range(50))
print(n)    # <filter object at 0x00000201972C28B0>


n = list(n)
print(n)
# => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]


""" lambda function
def double(val):
    return val*2

The above code can be shortened like this:

lambda val: val * 2

"""

(lambda x: x > 3)(4)  # => True

# Squares from 0**2 to 9**2
map(lambda val: val ** 2, range(10))
""" result: => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]"""

# Tuples with positive second elements
filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8,0)])

# Sort a collection based on a custom function.
sorted([(4,1), (3, -2), (8,0)], key=lambda pair: pair[1])
