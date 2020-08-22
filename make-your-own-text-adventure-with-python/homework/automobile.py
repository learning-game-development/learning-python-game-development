class Vehicle:
    def __init__(self):
        raise NotImplementedError("Do not create raw Vehicle objects.")

    def __str__(self):
        return "{} has {} wheels".format(self.name, self.wheels)


class Motorcycle(Vehicle):
    def __init__(self, name):
        self.name = name
        self.wheels = 2


class Car(Vehicle):
    def __init__(self, name):
        self.name = name
        self.wheels = 4

print(Motorcycle('Yamaha'))
print(Car('Ford Mustang'))
print(Vehicle())
