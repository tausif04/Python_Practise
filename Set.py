fruits={"apple","banana","cherry"}
print(fruits)

#adds an element to the set
fruits.add("Orange")
print(fruits)

# Update()=Adds multiple elements to the set
fruits.update(["grape","melons","guava"])
print(fruits)

#remove()=Removes the specified element from the set ,Raises a KeyError if the element is not found
fruits.remove("banana")
print(fruits)

#discars()=Discards the specified element from the set,raises a keyerror if the element is not found
fruits.discard("cherry")
print(fruits)

#pop()=Removes and returns an arbitary element from the set,raises a keyerror if the set is empty
last_fruit=fruits.pop()
print("poped element: ",last_fruit)
print(fruits)

#clear()=Removes all elements from the set
fruits.clear()
print(fruits)

#union=Return a new set with al elements from the sets
fruits={"apple","banana","cherry"}
set1={"banana","Lichie","cherry","orange","guauva"}
result=fruits.union(set1)
print("Union of set1 and fruits: ",result)#No duplicates: Sets do not allow duplicate elements

#intersection()=Return a new set with elements present in both sets
fruits={"apple","banana","cherry"}
set1={"banana","Lichie","cherry","orange","guauva"}
result=fruits.intersection(set1)
print("Intersection of set1 and fruits: ",result)#common elements: Sets allow duplicate elements

#difference()=Return a new set with elements present in the first set but not in the second set
fruits={"apple","banana","cherry"}
set1={"banana","Lichie","cherry","orange","guauva"}
result=fruits.difference(set1)
print("Difference of set1 and fruits: ",result)#elements present in fruits but not in set1: Sets allow duplicate elements

#symmetric_difference()=Return a new set with elements present in either the first set or the second set but not in both
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)

 #issubset()=Check if all elements of the set are present in another set and return boolean value
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.issubset(set2))

#issupperset()=Check if the set contain all elements of another set and return boolean value
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.issuperset({1,2,4}))
print(set2.issubset(set1))

#isdisjoint()=Check if two sets have no common elements and return boolean value
set1 = {1, 2, 3}
set2 = {6, 4, 5}
print(set1.isdisjoint(set2))

