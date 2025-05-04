def get_positive_integer():
    while True:
        try:
            user_input = int(input("Please enter a positive integer: "))
            if user_input > 0:
                return user_input
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

positive_integer = get_positive_integer()
print(f"You entered: {positive_integer}")
