# ---------------------------1.Immutable
# What is immutable: Strings in Python, just like in JavaScript, cannot be changed in place.
name = "Amanjeet"
# name[1] = "p"  # This line will raise a TypeError, as strings are immutable.
# To change the string, you must reassign the whole variable.
name = "rikky"
print(name)  # Output: rikky

# ------------------------2.Creating Strings
# How to create strings: Python also supports various methods for string creation.
# We can make strings using the following methods:
a = 'a'  # Using single quotes
b = "b"  # Using double quotes

# A unique feature of Python is triple quotes, used for multiline strings.
c = """c
This is a
multiline string."""
print(c)

# -----------------------3.Accessing Characters
# Strings are a set of characters.
# We can access characters using their index (position), which starts at 0.
name = "Amanjeet"
print(name[0])  # Output: A
print(name[2])  # Output: a
print(name[1])  # Output: m

# A powerful feature in Python is negative indexing.
# This allows you to access characters from the end of the string.
print(name[-1]) # Output: t (the last character)
print(name[-2]) # Output: e (the second to last character)