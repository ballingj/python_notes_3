"""
# Before code

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    return password != username and password not in INVALID_PASSWORDS


def create_account(username, password):
    return (username, password)


def main(username, password):
    valid = validate_password(username, password)

    if valid:
        account = create_account(username, password)
    else:
        print("Oh no!")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!
"""

# The after code

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

# define a new exception subclass


class InvalidPasswordError(ValueError):
    pass


# this function produces an InvalidPasswordError if the password is invalid
def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("username and password must be different!")
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError(
            "This password is in a list of most commonly used passwords.  Select a new one.")


def create_account(username, password):
    return (username, password)

# Main function


def main(username, password):
    try:
        validate_password(username, password)

    except InvalidPasswordError as err:
        print(err)

    else:
        account = create_account(username, password)

    finally:
        print("Password validated against username and collection.")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!

"""
# Class Solution

class InvalidPasswordError(ValueError):
    pass


INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError(
            "Password cannot be the same as your username.")
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError(
            "Password cannot one of the most common passwords.")


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as err:
        print(err)
    else:
        account = create_account(username, password)
    finally:
        print("Validated password against username and collection")

"""
