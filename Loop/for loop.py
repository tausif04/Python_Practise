#The for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects

#Iterating Over a List
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example of iterating over a string
word = "hello"
for letter in word:
    print(letter)

# Example of using range() function
"""The range() function defaults to 0 as a starting value, however it is possible to
 specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):"""
for x in range(2, 6):
  print(x)
for i in range(5):
    print(i)

"""The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):"""
for x in range(2, 30, 3):
  print(x)


# Example of iterating over a dictionary
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
for student, score in student_scores.items():
    print(f"{student}: {score}")

# Example of iterating over a set
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)

# Example of using break statement
for number in range(10):
    if number == 5:
        break
    print(number)

# Example of using continue statement
for number in range(10):
    if number == 5:
        continue
    print(number)