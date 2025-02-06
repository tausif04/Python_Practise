#The if statement executes a block of code if a specified condition is True
#The else statement executes a block of code if the if condition is False

age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# The elif statement allows you to check multiple conditions. It stands for "else if" and can be
# used when you need to check more than one condition
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")