def reverse_list(int_list):
    reversed_list = int_list[::-1]
    return reversed_list
list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(list)
print("Original list : ", list)
print("Reversed list : ", reversed_list)
