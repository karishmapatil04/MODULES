# Creating a Dog class
class Dog:
    # Class variable (common for all dogs)
    animal = "Dog"

    # Constructor with instance variables
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Method to display details
    def display_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Name:", self.name)
        print()

# Creating objects for two different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Max")

# Displaying details
dog1.display_details()
dog2.display_details()