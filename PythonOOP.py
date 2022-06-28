
"""
# Class and Objects
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("The configuration is:", self.cpu, self.ram)

comp1 = Computer("i5", 8)
comp2 = Computer("ryzen 3", 16)

comp1.config()
comp2.config()


# Constructor, Self and comparing objects

class Computer:
    def __init__(self):
        self.name = "Aman"
        self.age = 20
    def update(self):
        self.age = 15
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        
    
c1 = Computer()
c2 = Computer()

c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

#print(id(c1))
#print(id(c2))

#print(c1.name)
#print(c2.name)

print(c1.age)
print(c2.age)



# Types of Variables

class Car:
    wheels = 4                  # class or static variables
    def __init__(self):
        self.mil = 10           # object or instance variables
        self.comp = "BMW"       # object or instance variables

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)




# Types of methods


class Student:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):           # accessor
        return self.m1
    
    def set_m1(self, value):    # mutators
        self.m1 = value
        return self.m1

    @classmethod
    def get_school(cls):        # class method
        return cls.school

    @staticmethod
    def info():
        print("This is Student class...")

s1 = Student(31,76,23)
s2 = Student(23,24,29)

print(s1.avg())
print(s2.avg())

#print(s1.get_m1())
#print(s2.get_m1())
#print(s1.set_m1(40))
#print(s2.get_m1())

print(Student.get_school())
Student.info()




# inner class



class Student:                              # outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:                           # inner class
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        
        def show(self):
            print(self.brand, self.cpu, self.ram)


    
s1 = Student("Aman", 2)
s2 = Student("Abhi", 3)

s1.show()
s2.show()

# s1.lap.show()




# Inheritence

class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

class B(A):                     # Single-Level Inheritence B-> A
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(B):                     # Multi-Level Inheritence C-> B-> A
    def feature5(self):
        print("Feature 5 working")

class D:
    def feature6(self):
        print("Fearure 6 is working")

class E(A,D):                   # Multiple Inheritence
    def feature7(self):
        print("Feature 7 is working")
a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()
c1.feature3()
d1.feature6()




# Constructor in Inheritance and Method Resolution Order (MRO)

class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("feature 1 is working ")
    def feature2(self):
        print("feature 2 is working")


class B(A):
    def __init__(self):
        #super().__init__()
        print("init B")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

a1 = A()
b1 = B()



class C:
    def feature5(self):
        print("Fearure 5 working")
class D(A,C):
    def __init__(self):
        print("init D")
    def feature6(self):
        print("feature 6 is working")
    def feat(self):
        super().feature2()

d1 = D()
d1.feat()

"""