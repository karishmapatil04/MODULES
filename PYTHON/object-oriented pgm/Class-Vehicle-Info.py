# create class
class Vehicle:

	# create init method
    def __init__(self, max_speed, mileage):
		# bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
        print(max_speed)

    def display(self):
        print("max speed :",self.max_speed)

# Object creation
modelX = Vehicle(240, 18)
modelX.display()

# access the variables inside init method
#print("Model Max Speed:",modelX.max_speed)
#print("Model Mileage:", modelX.mileage)