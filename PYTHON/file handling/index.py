file = open("bucket-list.txt", "r")
lines = file.readlines()   # returns a list of lines
file.close()

# Count the lines
print(f"You have {len(lines)} items on your bucket list.")
# Output: You have 3 items on your bucket list.

# See what the list looks like:
print(lines)
# ['1. Visit the Eiffel Tower\n',
#  '2. Learn to play the guitar\n',
#  '3. Code my own game\n']