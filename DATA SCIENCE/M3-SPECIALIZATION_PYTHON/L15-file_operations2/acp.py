# 1. Create and write into file
file = open("student.txt", "w")
file.write("Name: Karishma\nAge: 20\n")
file.close()

# 2. Read the file
file = open("student.txt", "r")
print("Initial Content:")
print(file.read())
file.close()

# 3. Append new data
file = open("student.txt", "a")
file.write("Course: BCA\n")
file.close()

# 4. Read after append
file = open("student.txt", "r")
print("\nAfter Appending:")
print(file.read())
file.close()

# 5. Modify content using r+
file = open("student.txt", "r+")
content = file.read()
file.seek(0)
file.write(content.replace("Age: 20", "Age: 21"))
file.close()

# 6. Final read
file = open("student.txt", "r")
print("\nAfter Modification:")
print(file.read())
file.close()