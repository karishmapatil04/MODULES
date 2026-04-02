import math
from abc import ABC, abstractmethod

# Abstract Base Class
class Polygon(ABC):
    
    @abstractmethod
    def area(self):
        pass


# Rectangle Class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


# Square Class
class Square(Polygon):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2


# Triangle Class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# Circle Class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2


# Main Program with Menu
def main():
    while True:
        print("\n--- Area Calculator ---")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            shape = Rectangle(l, w)
        
        elif choice == '2':
            s = float(input("Enter side: "))
            shape = Square(s)
        
        elif choice == '3':
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            shape = Triangle(b, h)
        
        elif choice == '4':
            r = float(input("Enter radius: "))
            shape = Circle(r)
        
        elif choice == '5':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Try again.")
            continue
        
        print("Area =", shape.area())


# Run program
if __name__ == "__main__":
    main()