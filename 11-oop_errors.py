"""
# syntax

try:
    dangerous_code()
except SomeError:
    handle_the_error()
else: 
    handle_no_error()
finally:
    do_no_matter_what()


# Bare except blocks

def read_int():
    while True:
        try:
            return int(input("Pleae give me a number: "))
        except:
            print("Not a number!")
'''
A bare except block captures all exceptions, including subclasses of BaseException like KeyboardInterrupt 
or SystemExit! This means that you almost never want except: and instead want to capture a specific class 
of errors, like except ValueError:
'''

"""

# capture the ValueError specifically
def read_int():
    while True:
        try:
            return int(input("Pleae give me a number: "))
        except ValueError:
            print("Not a number!")

read_int()


# except and else blocks

try:
    distance = int(input("How far? "))
    car.travel(distance)
    car.rev()
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Bad division")
except (NameError, AttributeError):
    print("Bad name or attribute.")
else:
    print("success")

'''
# example only
try:
    update_the_database()
except TransactionError:
    rollback()
else:
    commit()
'''

# The finally block runs almost no matter what. 
# It's used to define unconditional clean-up actions, such as closing a file or releasing a system resource.

try:
    raise NotImplementedError
finally:
    print("GoodBye!")

