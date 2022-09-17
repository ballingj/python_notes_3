class Point:
    """Implement your Point class in here!"""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
        


if __name__ == '__main__':
    # This won't work until you finish implementing the Point class.
    origin = Point()  # Default to (0, 0)
    point = Point(4, 1)  # x = 4, y = 1
    other_point = Point(3, -3)
    # Ooh, our objects behave a bit like numbers that can be added!
    third_point = point + other_point

    print(origin)  # Point(0, 0)
    print(point)  # Point(4, 1)
    print(other_point)  # Point(3, -3)
    print(third_point)  # Point(7, -2)
    
    # print(point.x)
    # print(point.y)


"""
SOLUTION:

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

"""
