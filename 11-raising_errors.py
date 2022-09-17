"""
# Raise an instance of a BaseException subclass
raise NameError("Why hello!")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: Why hello!

# Raise a subclass of BaseException
raise NameError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError
"""

"""
# To define a custom type of error, subclass (directly or indirectly) from a built-in exception.

class MyCustomNameError(NameError):
    pass

# Now MyCustomNameError is a part of the hierarchy!

print(MyCustomNameError.mro())
# [MyCustomNameError, NameError, Exception, BaseException, object]

# Custom errors can be raised from this class

raise MyCustomNameError("My custom error")

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# MyCustomNameError: My custom error
"""

# This is important because it can let you define better, more specific names for specific exceptional circumstances:

class PreconditionError(ValueError):
    pass


class SSLError(OSError):
    pass


class EmptyDatasetError(RuntimeError):
    pass


class BadLoginError(KeyError):
    pass


#Then, we can informatively raise these errors, instead of their more generic counterparts:
raise BadLoginError("Missing password")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# BadLoginError: 'Missing password'

#Moreover, other clients can more specifically respond to these errors:
try:
    raise BadLoginError("No username :(")
except BadLoginError:  # Respond only to `BadLoginError`s, not other types of `KeyError`s.
    pass
