# My School Subject Planner

# Tuple to store student details
student = ("Rahul", 8, "A")

print("Student Details:", student)

# Access tuple values
print("Name:", student[0])
print("Class:", student[1])
print("Section:", student[2])

# Sets of subjects
monday = {"Math", "Science", "English"}
tuesday = {"English", "Computer", "Math"}

print("\nMonday Subjects:", monday)
print("Tuesday Subjects:", tuesday)

# Add a subject
monday.add("Hindi")
print("\nMonday after adding a subject:", monday)

# Remove a subject
monday.remove("Science")
print("Monday after removing a subject:", monday)

# Common subjects
print("\nCommon Subjects:", monday.intersection(tuesday))

# All subjects
print("All Subjects:", monday.union(tuesday))

# Subjects only on Monday
print("Only Monday Subjects:", monday.difference(tuesday))

# Subjects only on Tuesday
print("Only Tuesday Subjects:", tuesday.difference(monday))