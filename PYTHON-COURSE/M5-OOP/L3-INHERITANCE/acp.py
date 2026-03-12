# Parent class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

# Child class
class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    # Method to calculate total fare
    def total_fare(self):
        fare_per_person = 100
        total = self.capacity * fare_per_person
        return total

# Creating object
bus1 = Bus(50)

# Display result
print("Bus Capacity:", bus1.capacity)
print("Total Fare:", bus1.total_fare())