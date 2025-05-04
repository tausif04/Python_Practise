def sum_of_even_numbers(int_list):
    total = 0
    for num in int_list:
        if num % 2 == 0:
            total += num
    return total

numbers = []
length=int(input("Enter the lenth of the list: "))

for i in range(length):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Original list:", numbers)
print("Sum of even numbers:", sum_of_even_numbers(numbers))