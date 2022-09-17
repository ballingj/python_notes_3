"""
# Part 1:  GETTERS Property
class House:
    PRICE_PER_SQUARE_FOOT = 2.5
    def __init__(self, size, num_bedrooms, num_bathrooms):
        self.size = size
        self.beds = num_bedrooms
        self.baths = num_bathrooms
    @property
    def price(self):
        return self.size * self.PRICE_PER_SQUARE_FOOT

home = House(1000, 2, 2)

print(home.beds)    # => 1000
print(home.size)  # => 2
print(home.baths)  # => 2

# print(home.price())  # had to call a method to get a price
# add @property right above the method
print(home.price)
# => <bound method House.price of <__main__.House object at 0x7f618d3b8520>>

home = House(1000, 2, 2)

print(home.beds)    # => 1000
print(home.size)  # => 2
print(home.baths)  # => 2

# print(home.price())  # had to call a method to get a price
# add @property right above the method
print(home.price)
# => <bound method House.price of <__main__.House object at 0x7f618d3b8520>>

"""

# Part 2: Setters

class House:
    PRICE_PER_SQUARE_FOOT = 2.5

    def __init__(self, size, num_bedrooms, num_bathrooms):
        self.size = size
        self.beds = num_bedrooms
        self.baths = num_bathrooms

    @property
    def price(self):
        return self.size * self.PRICE_PER_SQUARE_FOOT
    
    @price.setter
    def price(self, new_price):
        self.size = new_price / self.PRICE_PER_SQUARE_FOOT

home = House(1000, 2, 2)

print(home.price)    # => 2500.0
print(home.size)  # => 100
home.price = 2000
print(home.size)  # => 800.0
