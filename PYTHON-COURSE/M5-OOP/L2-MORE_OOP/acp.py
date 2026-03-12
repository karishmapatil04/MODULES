import math

class Circle:
    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def area(self):
        return math.pi * self.radius * self.radius

    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# Creating object
c1 = Circle(5)

# Display results
print("Radius:", c1.radius)
print("Area of Circle:", c1.area())
print("Perimeter of Circle:", c1.perimeter())