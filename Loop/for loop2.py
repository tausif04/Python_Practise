#nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement->for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass


# Enumerate->In Python, the enumerate() function is used with the for loop to iterate over an iterable while also keeping track of the index of each item.

l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print (count, ele)

# Python for loop in One Line

Numbers =[x for x in range(11)]

for i ,j in enumerate(Numbers):
   print(i," : ",j)

