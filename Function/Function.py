import random

numbers=[]
for _ in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)
max_number = float('-inf')

#Linear Search
for n in numbers:
    if n>max_number:
        max_number = n

print(max_number)