def sort_accending(numbers):
    n=len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

numbers = [3, 6, 8, 10, 1, 2, 1, 5, 4, 9]
sorted_numbers = sort_accending(numbers)
print(sorted_numbers)