def extract_middle_elements(num_list):
    length = len(num_list)

    if length % 2 == 1:
        middle_index = length // 2
        return num_list[middle_index]
    else:
        middle_index1 = (length // 2) - 1
        middle_index2 = length // 2
        return num_list[middle_index1:middle_index2 + 1]

numbers = list(map(int,input("Enter the numbers of the list (separated by spaces) :").split()))

middle_elements = extract_middle_elements(numbers)

print("Original list:", numbers)
print("Middle element(s):", middle_elements)