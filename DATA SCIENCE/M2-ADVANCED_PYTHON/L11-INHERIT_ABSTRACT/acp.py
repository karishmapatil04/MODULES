import math

# Base class
class Polygon:
    def area(self):
        pass   # to be overridden by subclasses


# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2


# Main program
print("Choose a shape:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter your choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    shape = Rectangle(l, w)

elif choice == 2:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    shape = Triangle(b, h)

elif choice == 3:
    r = float(input("Enter radius: "))
    shape = Circle(r)

else:
    print("Invalid choice!")
    shape = None

if shape:
    print("Area:", shape.area())