#Uses of FINALLY block
try:
# Code that may raise an exception
    with open("example.txt") as file:
        content = file.read()
    result = 10 / int(content)
except ZeroDivisionError:
# Handle the division by zero error
    print("Error: Cannot divide by zero.")
finally:
# This block will be executed no matter what
    print("Execution completed.")



