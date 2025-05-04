#String Methods

# Define a string for demonstration
text = "hello world"

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
text = "HELLO WORLD"
print("Lowercase:", text.lower())

# Capitalize the first letter
text = "hello world"
print("Capitalize:", text.capitalize())

# Title case (capitalize first letter of each word)
print("Title case:", text.title())

# Swap case (invert case of each letter)
text = "Hello World"
print("Swap case:", text.swapcase())

# Replace a substring
text = "hello world"
print("Replace:", text.replace("world", "Python"))

# Split the string into a list
text = "hello-world"
words = text.split("-")

# Join a list into a string
words = ['hello', 'world']
print("Join:", ' '.join(words))

# Strip whitespace from both ends
text = " hello world "
print("Strip:", text.strip())
# Remove leading whitespace
print("Left strip:", text.lstrip())
# Remove trailing whitespace
print("Right strip:", text.rstrip())

# Check if string starts with a substring
text = "hello world"
print("Starts with 'hello':", text.startswith("hello"))
# Check if string ends with a substring
print("Ends with 'world':", text.endswith("world"))
# Find the position of a substring
print("Find 'world':", text.find("world"))
# Count occurrences of a substring
print("Count 'o':", text.count("o"))
# Check if all characters are alphanumeric
print("Is alphanumeric:", text.isalnum())


# Check if all characters are alphabetic
text = "hello"
print("Is alphabetic:", text.isalpha())

# Check if all characters are digits
text = "12345"
print("Is digit:", text.isdigit())

text = " "
print("Is whitespace:", text.isspace())

# Check if the string is titlecased
text = "Hello World"
print("Is titlecased:", text.istitle())

# Example of combining methods
# Capitalizing each word in a sentence
sentence = "this is a sample sentence."
capitalized_sentence = sentence.title()
print("Capitalized sentence:", capitalized_sentence)

# Removing extra spaces and converting to uppercase
text = " hello world "
cleaned_text = text.strip().upper()
print("Cleaned and uppercase:", cleaned_text)