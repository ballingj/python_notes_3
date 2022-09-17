"""
In this exercise, you'll write a function called generate_cases that represents an infinite stream of random lists of increasing size.

g = generate_cases()
next(g)  # => []
next(g)  # => [5]
next(g)  # => [3, 1]
next(g)  # => [1, 7, 4]
next(g)  # => [2, 2, 9, 0]
# ... and on and on.

You'll be able to use the function helper.random_list, which produces a random list of a given size with values between a inclusive start and exclusive stop integer (defaulting to 0 and 10). That is, helper.random_list(5) might produce [4, 8, 1, 1, 3].

This means that your function should be compatible with the following code snippet that prints out random lists up to size 10:

for case in generate_cases():
    if len(case) > 10:
        break
    print(case)

Functions like this one can be used in automated fuzz-testing scenarios, where an infinite stream of random-but-realistic looking data is used to automatically probe the behavior of some functionality under test.

"""
import random


def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))


'''Generate an infinite stream of successively larger random lists.'''
def generate_cases():
    num = 0
    while True:
        cases = random_list(num)
        num += 1
        yield cases


if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)

'''
# sample expected output
[]
[2]
[6, 4]
[9, 9, 1]
[4, 1, 1, 7]
[3, 9, 6, 4, 1]
[5, 6, 7, 8, 1, 8]
[1, 7, 9, 9, 4, 9, 8]
[3, 9, 4, 5, 7, 1, 3, 1]
[1, 4, 3, 8, 5, 0, 9, 4, 3]
[8, 5, 1, 1, 8, 6, 5, 3, 1, 6]


'''

'''
#Alternative solution is to use builtin function itertools.count() that generates a count 1,2,3,4,5,...

import itertools
import helper

def generate_cases_alternative():
    return (helper.random_list(size) for size in itertools.count())

def generate_cases_another_alternative():
    return map(helper.random_list, itertools.count())

'''
