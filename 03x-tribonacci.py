# Tribonacci Numbers
"""
The Tribonacci numbers are defined recursively, like the Fibonacci numbers, except that each subsequent number 
is the sum of the previous three. The first three Tribonacci numbers are 0, 0, 1. The next Tribonacci numbers 
in the sequence are 1, 2, 4, 7, 13, 24, 44, 81, ...

Write a generator function generate_tribonacci_numbers that generates an infinite stream of Tribonacci numbers. 
It will look very similar to the generate_fibs function we saw previously.
Then, write a function is_tribonacci that checks if a given number is a Tribonacci number. Be careful!
 You'll need to stop your search for a match if the Tribonacci number you're generating get too big. 
 Specifically - the implementation return num in generate_tribonacci_numbers() will work fine when the number 
 is a Tribonacci number, but will continue infinitely if not.
"""


def generate_tribonacci_numbers():
    """Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a."""
    a, b, c = 0, 0, 1
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
    while True:
        a, b, c = b, c, a + b + c
        yield a


def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    for trib in generate_tribonacci_numbers():  # loops over 0, 0, 1, 1, 2, 4, 7, 13, 24...
        if trib == num:
            return True
        elif trib > num:
            return False    
    
"""
# Lesson Solution

def is_tribonacci(num):
    '''Return whether `num` is a Tribonacci number.'''
    for n in generate_tribonacci_numbers():
        if n < num:
            continue
        return n == num
"""

print(is_tribonacci(2)) #True
print(is_tribonacci(9)) #False
print(is_tribonacci(13))  # True
print(is_tribonacci(24))  # True
print(is_tribonacci(225))  # False
print(is_tribonacci(109))  # False
