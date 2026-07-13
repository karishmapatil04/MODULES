# Robot Introduction using OOP

class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print("Hello!")
        print("My name is", self.name)
        print("My color is", self.color)
        print("I am your friendly robot.")

# Create an object
robot1 = Robot("Robo", "Blue")

# Call the method
robot1.introduce()