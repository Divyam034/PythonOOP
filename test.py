"""
# Class and Objects
class Computer:
    def __init__(self, cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Configuration is: ", self.cpu, self.ram)

comp1 = Computer("i5",8)        # Constructor
comp2 = Computer("i7",16)
comp3 = Computer("Ryzen 5", 32)

comp1.config()
comp3.config()


# Comparting objects

class Computer:
    def __init__(self):
        self.name = "Asus"
        self.ram = 16
    def info(self):
        print("information of Computer is: ", self.name, self.ram)
    def compare(self, other):
        if self.ram == other.ram:
            return True
        else:
            return False
    def update(self, ram):
        self.ram = ram
c1 = Computer()
c2 = Computer()


c1.info()
c2.info()
c2.update(8)
print(c1.compare(c2))

"""

# Types of variables

class Car:
    wheels = 5                                  # Class Variable / Static Variable
    def __init__(self, name, fuelType):
        self.name = name                        # Object Variable / Instance Variable
        self.fuelType = fuelType

c1 = Car("BMW", "CNG")
c2 = Car("Audi", "Solar")
Car.wheels = 4
c1.name = "Mercedes"
print(c1.name)
print(c1.wheels)


# Types of Methods
