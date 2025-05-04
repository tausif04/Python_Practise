def get_positive_integer():
    while True:
        try:
            user_input = int(input("enter a positive integer: "))

            if user_input > 0:
                print(f"Thank you! for entered a valid positive integer: {user_input}")
                break
            else:
                print("Error: The number must be positive. Try again.")

        except ValueError:
            print("Error!!! Please enter a valid integer.")

get_positive_integer()