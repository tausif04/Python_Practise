try:
# Code that may raise an exception
    with open("example.txt") as file:
        content = file.read()
    result = 10 / int(content)
except ZeroDivisionError:
# Handle the division by zero error
    print("Error: Cannot divide by zero.")
except FileNotFoundError:
# Handle the file not found error
    print("Error: File not found.")
except ValueError:
# Handle the error if content is not a valid integer
    print("Error: File content is not a valid number.")
else:
# This block will be executed if no exceptions occur
    print("Division successful, result is:", result)
finally:
# This block will be executed no matter what
    print("Execution completed.")