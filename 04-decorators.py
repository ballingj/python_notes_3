import functools

def perform_twice(fn, *args, **kwargs):
    fn(*args, **kwargs)
    fn(*args, **kwargs)


perform_twice(print, 5, 10, sep='&', end='...\n')
# 5&10...5&10...


def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n


div_by_3 = make_divisibility_test(3)
tuple(filter(div_by_3, range(10)))  # => (0, 3, 6, 9)

make_divisibility_test(5)(10)  # => True


def print_args(function):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)
    return wrapper

# This decorator captures a function, and creates and returns a new function named wrapper. The wrapper function captures any collection of
# arguments, prints them out, and then forwards them to the supplied function. Let's take a look at this decorator in action


def compute(x, y, z=1):
    return (x + y) * z

compute(3, 5, z=2)
# => 16

compute_log = print_args(compute)
print(compute_log(3, 5, z=2))
# (3, 5) {'z': 2}
# => 16

# Wow! We modified a function to build a new one that can print out its arguments. It'd be a bit of a pain to refactor the rest of the codebase to use compute_log instead of compute, so let's just rename compute itself.
compute = print_args(compute)
print(compute(4, 5, z=3))
# (4, 5) {'z': 3}
# => 27


def print_args2(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)
    return wrapper


@print_args2
def compute2(x, y, z=1):
    return (x + y) * z

#compute2 = print_args2(compute2)   # not needed with @decorator
print(compute2(5, 6, z=1))
#(5, 6) {'z': 1}
# => 11
