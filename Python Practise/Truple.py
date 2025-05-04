fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0]) # Output: apple
print(fruits[1]) # Output: banana
print(fruits[2]) # Output: cherry

#Truple methods
#count=returns the number of times a specified value appears in the truple
numbers=(1,2,3,2,4,2)
count_of_two=numbers.count(2)
print("The count of twos : ",count_of_two)

#index=returns the index of the forst occurrence of the specified value
index_of_three=numbers.index(3)
print(index_of_three)

# You can loop through the elements of a tuple using a for loop
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

#Truple Slicing=You can access a range of elements in tuple using slicing
fruits = ("apple", "banana", "cherry")
print(fruits[1:3]) # Output: ('banana', 'cherry')
print(fruits[:2]) # Output: ('apple', 'banana')
print(fruits[1:]) # Output: ('banana', 'cherry')
print(fruits[-2:]) # Output: ('banana', 'cherry')


# Converting Between Lists and Tuples
# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple) # Output: (1, 2, 3)

# Tuple to list
my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print(my_list) # Output: [4, 5, 6]



