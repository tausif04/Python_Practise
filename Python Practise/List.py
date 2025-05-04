fruits = ["apple", "banana", "cherry"]
print(fruits)

#append=adds element to the end of the list
fruits.append("Guava")
print(fruits)

#insert=inserts an element at a specified position
fruits.insert(2,"Orange")
print(fruits)

#extend=Extends the list by adding elements from another list.
more_fruits=["Mango","Lichi","grape"]
fruits.extend(more_fruits)

#remove=Removes the first occurrence of the specified element
fruits.remove("banana")
print(fruits)

# Pop=Removes the element at the specified position(default is the last element) and return it
last_fruit=fruits.pop()
print(last_fruit)
print(fruits)

# clear=Removes all element from the list
fruits.clear()
print(fruits)


fruits = ["apple", "banana", "cherry"]
# Index=returns the number of occurence of the specified element
index=fruits.index("banana")
print("The Index of banana is : ",index)


more_fruits=["Mango","Lichi","grape","banana","Orange","Drangon"]
fruits.extend(more_fruits)
#Count=returns the number of occuurrences of the specified element
count=fruits.count("banana")
print(count)

# Reverse=reverse the order of the list
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.reverse()
print(numbers)

# len()=returns the number of the element in the list
fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(length)

# List Slicing=you can access a range of element using slicing
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(fruits[1:4]) # ['banana', 'cherry', 'date']
print(fruits[:3]) # ['apple', 'banana', 'cherry']
print(fruits[3:]) # ['date', 'fig', 'grape']
print(fruits[-3:]) # ['date', 'fig', 'grape']

# Looping through a list
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
for fruit in fruits:
    print(fruit)