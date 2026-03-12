class StringReverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()        # Split the string into words
        reversed_words = words[::-1]    # Reverse the list of words
        return " ".join(reversed_words) # Join them back into a string


# Creating object
s1 = StringReverse("Python is very easy")

# Display result
print("Original String:", s1.text)
print("Reversed String:", s1.reverse_words())