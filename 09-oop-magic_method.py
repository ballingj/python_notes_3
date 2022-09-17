class MagicShoppingCart:
    def __init__(self, items):  # items will be a dictionary
        self.items = items

    def __len__(self):  # the value in key: value pair will be a string, so calculate the number of items in the cart 
        return sum(self.items.values())

    def __str__(self):  #
        return f"MagicShoppingCart({self.items})"

    def __contains__(self, item):
        return item in self.items

    def __iadd__(self, other):
        for item, count in other.items.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count
        return self

cart = MagicShoppingCart({'apples': 3, 'bananas': 2})   

# __len__ method
len(cart)  # returns 5 -- this is possible because of the __len__ method we added to the class

# __str__ method allows to return the literal string of the object 
print(cart)  # returns "MagicShoppingCart({'apples': 3, 'bananas': 2})" the literal text of the object due to 

# __contains__ method above allows us to search if an item is in a cart
print('apples' in cart)  # True
print('oranges' in cart)  #False

# __iadd__ method allows to add two shopping cart objects together
second_cart = MagicShoppingCart({'apples': 2, 'oranges': 5})

cart += second_cart

# shows the union of cart and second_cart
print(cart)  # returns "MagicShoppingCart({'apples': 5, 'bananas': 2, 'oranges': 5})"



"""
Reference for more Magic Methods:
https://rszalski.github.io/magicmethods/

"""
