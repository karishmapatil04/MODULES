# My Library Book Organiser

# List of books
books = ["Harry Potter", "Python Basics", "The Alchemist", "Matilda"]

print("Book List:", books)

# Add a new book
books.append("Wings of Fire")
print("\nAfter Adding:", books)

# Remove a book
books.remove("Matilda")
print("After Removing:", books)

# Sort the list
books.sort()
print("Sorted List:", books)

# Reverse the list
books.reverse()
print("Reversed List:", books)

# Indexing
print("\nFirst Book:", books[0])

# Slicing
print("First Three Books:", books[:3])

# Dictionary of librarian details
librarian = {
    "Name": "Anita",
    "Age": 35,
    "Library": "City Library"
}

print("\nLibrarian Details:")
print(librarian)

# Access dictionary value
print("Librarian Name:", librarian["Name"])

# Add a new key
librarian["Experience"] = "10 Years"

# Update a value
librarian["Age"] = 36

print("Updated Librarian Details:", librarian)

# Convert two lists into a dictionary
book_ids = [101, 102, 103]
book_names = ["Python", "Java", "C++"]

book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:")
print(book_directory)