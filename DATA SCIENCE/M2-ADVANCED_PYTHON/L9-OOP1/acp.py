# Define a class
class Robot:
    
    # Constructor
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    # Method to introduce the robot
    def introduce(self):
        print("Hello! My name is", self.name)
        print("I am a", self.model, "model robot.")
        print("I was created in", self.year)
    
    # Method to perform an action
    def perform_task(self, task):
        print(self.name, "is performing:", task)


# Create objects
robot1 = Robot("RoboX", "AI-2025", 2025)
robot2 = Robot("MechaZ", "AI-2024", 2024)

# Call methods
robot1.introduce()
robot1.perform_task("Cleaning")

print()

robot2.introduce()
robot2.perform_task("Cooking")