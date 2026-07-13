# My Pet Care Dashboard

# Parent class
class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health   # Private variable

    # Setter method
    def set_health(self, health):
        self.__health = health

    # Getter method
    def get_health(self):
        return self.__health

    def sound(self):
        print("Pet makes a sound.")

# Child class
class Dog(Pet):
    def sound(self):
        print(self.name, "says: Woof Woof")

# Child class
class Cat(Pet):
    def sound(self):
        print(self.name, "says: Meow Meow")

# Child class
class Bird(Pet):
    def sound(self):
        print(self.name, "says: Tweet Tweet")

# Create objects
pets = [
    Dog("Buddy", "Healthy"),
    Cat("Kitty", "Healthy"),
    Bird("Coco", "Healthy")
]

# Update health using setter
pets[0].set_health("Needs Checkup")

# Polymorphism
for pet in pets:
    pet.sound()
    print("Health:", pet.get_health())
    print()