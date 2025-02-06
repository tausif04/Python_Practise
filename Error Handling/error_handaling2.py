#Handling Mutiple Exception
try:
        # Attempt to read a non-existent file and divide by a non-numeric value
    with open("non_existent_file.txt") as file:
        content = file.read()
    result = 10 / int(content) # Assuming the content should be an integer
except FileNotFoundError:
# Handle the file not found error
    print("Error: File not found.")
except ValueError:
# Handle the error if content is not a valid integer
    print("Error: File content is not a valid number.")
except ZeroDivisionError:
# Handle the division by zero error
    print("Error: Cannot divide by zero.")



# Catching All Exceptions
try:
# Code that may raise an exception
    with open("example.txt") as file:
        content = file.read()
    result = 10 / int(content)
except Exception as e:
# Handle any exception
    print(f"An error occurred: {e}")

    