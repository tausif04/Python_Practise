import copy  

a = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the nested list 'original'
b = copy.copy(a)

# Modifying an element in the shallow-copied list
b[0][0] = 99

# Printing the original and shallow-copied lists
print(f"The Original: {a}") 
print(f"Shallow Copy : {b}")

# Deep copy
deep_copied = copy.deepcopy(b)

# Modify the nested list
deep_copied[0][0] = 99

print("The Original:", b) 
print("Deep Copy:", deep_copied)  