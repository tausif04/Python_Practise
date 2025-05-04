def count_element(numbers, element):
    count = 0
    for num in numbers:
        if num == element:
            count += 1
    return count

numbers = list(map(int,input("Enter the numbers of the list (separated by spaces)").split()))
element = int(input("Enter the element:"))
count = count_element(numbers, element)
print(f"The number {element} appears {count} times in the list.")