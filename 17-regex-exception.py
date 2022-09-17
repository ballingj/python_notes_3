import re


def validate_email(email):
    """ Test if an email is of a valid format """

    if type(email) is not str:
        raise Exception('Email is not a String')

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex, email):
        raise Exception('Email is Malformed')

    return True


email_address = 'hello@udacity.com'
try:
    if validate_email(email_address):
        print("Great Email")
except:
    print("Bad Email Address")
