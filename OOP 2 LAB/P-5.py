def multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

user_number = int(input("Enter a number: "))

multiplication_table(user_number)