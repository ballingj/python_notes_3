
# wrong way to add appliance
'''
class House:
    appliances = []

    def __init__(self, size):
        self.size = size

    def install(self, appliance):
        self.appliances.append(appliance)
'''
# correct way to add appliance
class House:
    def __init__(self, size):
        self.size = size
        self.appliances = []  # make it a part of instantiation

    def install(self, appliance):
        self.appliances.append(appliance)


home = House(1000)
vacation_home = House(5000)

home.install('oven')
home.install('microwave')
print(home.appliances)  # ['oven', 'microwave'] - good! what we wanted
# ['oven', 'microwave'] - oh no! we didn't want this
print(vacation_home.appliances)

print(id(home.appliances))  # => 45...1632
print(home.__dict__)  # {'size': 1000}
print(House.__dict__)
# {
#     'appliances': ['oven', 'microwave']
#     ... other stuff
# }

print(House.appliances)  # ['oven', 'microwave']
print(id(House.appliances))  # 45...1632
print(id(vacation_home.appliances))  # 45...1632

