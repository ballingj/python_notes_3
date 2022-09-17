"""
There are two other intriguing method decorators built into Python: classmethod and staticmethod

The @classmethod decorator changes method call behavior by passing the class object, not the instance object, as the first argument.
 Class methods are a useful technique for representing factory functions - other ways to create instance objects, but attached to the class itself.

The @staticmethod decorator changes method call behavior by not supplying either the instance object nor the class object as the first argument.
Static methods are a useful technique for attaching utility functions to a class.
 If you thing you can build a function that could be a separate function and not part of the class, it could be a static method
 
"""
class House:
    def __init__(self, size, num_bedrooms, num_bathrooms):
        self.size = size
        self.beds = num_bedrooms
        self.baths = num_bathrooms

    @classmethod
    def create(cls, description):
        """The description is 'SIZE BEDS BATH """
        size, beds, baths = description.split(' ')
        #Make a house using these values.
        return cls(float(size), int(beds), int(baths))
    
    @staticmethod
    def build_door(width, height):
        return (width, height)

# we made a class method
print(House.create)  # => <bound method House.create of <class '__main__.House'>>

home = House.create("1000 2 2")
print(home)  # => <__main__.House object at 0x7faffde4c280>

print(home.size)
print(home.beds)
print(home.baths)


print(House.build_door)  # => <function House.build_door at 0x7f3bebf27c70>

print(home.build_door)  # => <function House.build_door at 0x7f3bebf27c70>
