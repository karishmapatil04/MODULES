# Basic Calculations - Marks and Percentage

# Taking student details
name = input("Enter student name: ")

# Taking marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculating total marks
total_marks = sub1 + sub2 + sub3 + sub4 + sub5

# Calculating percentage
percentage = (total_marks / 500) * 100

# Displaying result
print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")