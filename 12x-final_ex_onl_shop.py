"""
Online Shopping

In this exercise, you'll start designing models for an online shopping service. Concretely, you'll need to build three classes:

    A User will have an id and a name, and be able to sell_product, buy_product, and write_review.
    A Product will contain a name, a description, a seller, a collection of reviews, a price, and an availability.
    A Review will contain a description, a user (who wrote the review), and a product (for which the review is written)

Each of these classes should be nicely printable.

By the time you're done, the following lines of code should be valid:

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True

In this exercise, we're less concerned with the precise specification of each of the objects. Part of your job as a programmer is to select object designs from among many options, according to whatever needs you (or your team) foresee.

Instead, as you are developing these classes, take some time to reflect on your own process for designing interconnected classes. We've seen lots of ways in which objects can fit together. Which ones make the most sense to you? Why? This is an exercise in self-reflection as much as it is in programming. Keep an eye out for object-based design patterns (such as implementing a __str__ method) that are particularly helpful for debugging.


"""

# user.py
# from review import Review
# from product import Product
"""

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def sell_product(self, name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f"{product} is on the market!")
        return product

    def buy_product(self, product):
        if product.available:
            print(f"{self} is buying the {product}.")
            product.available = False
        else:
            print(f"{product} is no longer available.")

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        print(f"{self.name}'s review of {product.name}: {review.content}")
        return review

    def __str__(self):
        return f"User(id={self.id}, name={self.name})"


# review.py
class Review:
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review of {self.product} by {self.user}: '{self.content}'"

# product.py
class Product:
    def __init__(self, name, description, seller, price, available):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.reviews = []
        self.available = available
    def __str__(self):
        return f"Product({self.name}: {self.description}) at ${self.price}"


brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True
"""



# product.py
class Product:
    def __init__(self, name, description, seller, price, available):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = available

    def __str__(self):
        return f"Product({self.name}, {self.description}) at ${self.price}"


# review.py

class Review:
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review of {self.product} by {self.user}: '{self.content}'"


# user.py
'''
from product import Product
from review import Review
'''
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        print(f"{self.name}'s review of {product.name}: {review.content}")
        return review

    def sell_product(self, name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f"{product} is on the market!")
        return product

    def buy_product(self, product):
        if product.available:
            print(f"{self} is buying {product}.")
            product.available = False
        else:
            print(f"{product} is no longer available.")

    def __str__(self):
        return f"User(id={self.id}, name={self.name})"


brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True
