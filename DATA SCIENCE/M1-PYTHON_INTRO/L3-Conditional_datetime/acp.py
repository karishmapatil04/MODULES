# Taking input from user
classes_held = int(input("Enter total number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

# Calculating attendance percentage
attendance = (classes_attended / classes_held) * 100

print("\nAttendance Percentage:", attendance, "%")

# Checking eligibility
if attendance >= 75:
    print("You are eligible to sit for the exam.")
else:
    print("You are NOT eligible to sit for the exam.")