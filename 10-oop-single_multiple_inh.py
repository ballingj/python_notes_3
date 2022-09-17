class MotorVehicle:
    def __init__(self, range):
        self.range = range
        self.tank = range

    def travel(self, distance):
        if distance > self.tank:
            print(
                f"Not enough in the tank. Only traveled {self.tank} kilometers.")
            self.tank = 0
        else:
            print(f"VOOOM! Traveled {distance} kilometers.")
            self.tank -= distance

    def refuel(self):
        print("Refueling...")
        self.tank = self.range

    def __str__(self):
        return(f"Vehicle(range={self.range}, tank={self.tank})")


mv = MotorVehicle(100)
print(mv)  # Vehicle(range=100, tank=100)
mv.travel(50)  # VOOOM! Traveled 50 kilometers.
mv.travel(30)  # VOOOM! Traveled 30 kilometers.
mv.travel(30)  # Not enough in the tank. Only traveled 20 kilometers.
print(mv)  # Vehicle(range=100, tank=0)
mv.refuel()  # Refueling...
print(mv)  # Vehicle(range=100, tank=100)

"""
class Car(MotorVehicle):
    def __init__(self, range, wheels, color):
        super().__init__(range)
        self.wheels = wheels
        self.color = color

# use the Car class inherited properties from MotorVehicle class
c = Car(500, 4, 'red')
print(c.range)  # 500
print(c.tank)  # 500
print(c.wheels)  # 4
print(c.color)  # 'red'
print(c.__dict__)  # {'range': 500, 'tank': 500, 'wheels': 4, 'color': 'red'}
c.travel(50)  # VOOOM! Traveled 50 kilometers.
c.travel(100)  # VOOOM! Traveled 100 kilometers.
c.refuel()  # Refueling...
print(c)  # Vehicle(range=500, tank=500)

"""

# let's add another custom method
class Car(MotorVehicle):
    def __init__(self, range, wheels, color):
        super().__init__(range)
        self.wheels = wheels
        self.color = color

    def __str__(self):
        return f"Car(range={self.range}, tank={self.tank}, wheels={self.wheels}, color={self.color})"


c = Car(500, 4, 'blue')
print(c)  # Car(range=500, tank=500, wheels=4, color=blue)


# We can create another subclass of MotorVehicle - this time, it'll be Motorcycle
class Motorcycle(MotorVehicle):
    def rev(self):
        print("REVVVVVVVV")


mc = Motorcycle(100)
print(mc.range)  # 100
print(mc.tank)  # 100
mc.travel(50)  # VOOOM! Traveled 50 kilometers.
mc.rev()  # REVVVVVVVV
print(mc)  # Vehicle(range=100, tank=50)
