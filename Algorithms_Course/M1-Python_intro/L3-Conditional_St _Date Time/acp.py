# My Daily Mood Advisor

from datetime import datetime

# Get current date and time
current_time = datetime.now()

# User input
name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/stressed/tired): ").lower()
energy = int(input("Enter your energy level (1-10): "))

# Display current date and time
print("\nCurrent Date and Time:", current_time.strftime("%d-%m-%Y %H:%M:%S"))

# Personalized advice
print("\nHello,", name + "!")

if mood == "happy":
    print("Keep smiling and spread your positivity!")
elif mood == "sad":
    print("Take some time to relax and talk to someone you trust.")
elif mood == "stressed":
    print("Take a short break, breathe deeply, and organize your tasks.")
elif mood == "tired":
    print("Get some rest, drink water, and recharge yourself.")
else:
    print("Have a wonderful day and take good care of yourself!")

# Energy level advice
if energy >= 8:
    print("You have high energy! It's a great day to be productive.")
elif energy >= 5:
    print("Your energy is moderate. Balance work with short breaks.")
else:
    print("Your energy is low. Take some rest and don't overwork yourself.")