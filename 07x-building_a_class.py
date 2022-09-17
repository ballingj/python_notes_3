"""
We've seen a lot of information about class objects, instance objects, and the various ways to resolve attributes on each, as well as the semantic behavior of method invocation, and a few modifications in the form of method decorators.

Now, you'll put together all of these concepts to build a Customer class that supports the following interface:

marco = Customer('Marco', 'Polo')  # Defaults to the free tier
print(marco.name)  # Marco Polo
print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
print(victoria.name)  # Alexandrina Victoria

A few hints and clarifications:

    The name can be a gettable property
    The tier defaults to ('free', 0)


"""

class Customer:
    def __init__(self, first_name, last_name, tier='free'):
        self.first_name = first_name
        self.last_name = last_name
        self.tier = tier
    @property
    def name(self):
        return self.first_name + " " + self.last_name
    
    @classmethod    
    def premium(cls, *args, tier='premium'):
        return cls(*args, tier)
    
    @staticmethod
    def bill_for(num_month):
        BILL_PER_MONTH = 10
        return BILL_PER_MONTH * num_month
    
    #@staticmethod
    def can_access(self, dict):
        #print(self.name, self.tier)
        if self.tier == 'free':
            #print(dict['tier'])
            if dict['tier'] == 'free':
                return True
            else:
                return False
        if self.tier == 'premium':
            if dict['tier'] == 'free':
                return True
            else:
                return True
    
if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!

    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    # Build a customer around the ('premium', 10$/mo) streaming plan.
    victoria = Customer.premium("Alexandrina", "Victoria")
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria



"""
Solutions:

class Customer:
    def __init__(self, first_name, surname, tier=('free', 0)):
        self.first_name = first_name
        self.surname = surname
        self._tier = tier[0]
        self._cost = tier[1]

    def bill_for(self, months):
        return months * self._cost

    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier

    @property
    def name(self):
        return f"{self.first_name} {self.surname}"

    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, tier=('premium', 10))
"""
