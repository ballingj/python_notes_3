"""
class House:
    PRICE_PER_SQUARE_FOOT = 2.5

    def __init__(self, size):
        self.size = size
        
    @property
    def price(self):
        return self.size * self.PRICE_PER_SQUARE_FOOT

    @price.setter
    def price(self, new_price):
        self.size = new_price / self.PRICE_PER_SQUARE_FOOT


home = House(10000)

print(home.size)  # => 10000
print(home.price)    # => 25000.0

print(home.PRICE_PER_SQUARE_FOOT)  # => 2.5

print(home.size)  # => 800.0
"""

# use underscore to denote do not change the property
class House:
    __PRICE_PER_SQUARE_FOOT = 2.5   # two _ _ or dunder

    def __init__(self, size):
        self._size = size       # quasi_private

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self.size * self.__PRICE_PER_SQUARE_FOOT

    @price.setter
    def price(self, new_price):
        self._size = new_price / self.__PRICE_PER_SQUARE_FOOT


home = House(10000)

print(home.size)  # => 10000
print(home.price)    # => 25000.0

# print(home.__PRICE_PER_SQUARE_FOOT)  # => Error: AttributeError: 'House' object has no attribute '__PRICE_PER_SQUARE_FOOT'. Did you mean: '_House__PRICE_PER_SQUARE_FOOT'

print(home.size)  # => 10000.0
