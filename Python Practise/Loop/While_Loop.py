# Iterating over a list with a while loop
fruits = ['apple', 'banana', 'cherry']
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# Iterating over a string with a while loop
word = "hello"
index = 0
while index < len(word):
    print(word[index])
    index += 1

# Simulating range() with a while loop
start = 0
end = 5
while start < end:
    print(start)
    start += 1

# Iterating over a dictionary with a while loop
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
keys = list(student_scores.keys())
index = 0
while index < len(keys):
    key = keys[index]
    print(f"{key}: {student_scores[key]}")
    index += 1

# Iterating over a dictionary with a while loop
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
keys = list(student_scores.keys())
index = 0
while index < len(keys):
    key = keys[index]
    print(f"{key}: {student_scores[key]}")
    index += 1

# Using break statement in a while loop
counter = 0
while counter < 10:
    if counter == 5:
        break
    print(counter)
    counter += 1

# Using continue statement in a while loop
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)

