# First create and write into file
file = open("data.txt", "w")
file.write("Hello Karishma\nWelcome to Python File Handling\nHave a nice day!")
file.close()

# 1. Read entire file
file = open("data.txt", "r")
print("1. Read Full File:")
print(file.read())
file.close()

# 2. Read one line
file = open("data.txt", "r")
print("\n2. Read One Line:")
print(file.readline())
file.close()

# 3. Read all lines as list
file = open("data.txt", "r")
print("\n3. Read All Lines (List):")
print(file.readlines())
file.close()

# 4. Read file using loop
file = open("data.txt", "r")
print("\n4. Read Using Loop:")
for line in file:
    print(line.strip())
file.close()