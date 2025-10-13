from abc import ABC, abstractmethod

class Polygon(ABC):
    """
    Abstract base class for all polygons.
    """
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Main program
if __name__ == "__main__":
    while True:
        print("\nChoose a polygon to calculate the area:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rect = Rectangle(length, width)
            print(f"The area of the rectangle is {rect.area()}.")

        elif choice == '2':
            side = float(input("Enter the side of the square: "))
            square = Square(side)
            print(f"The area of the square is {square.area()}.")

        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            triangle = Triangle(base, height)
            print(f"The area of the triangle is {triangle.area()}.")

        elif choice == '4':
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"The area of the circle is {circle.area()}.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")