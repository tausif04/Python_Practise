def create_list():
    size = int(input("Enter the size of the list:"))
    num_list = []
    for i in range(size):
        user_input = input("Enter value for list: ")
        num_list.append(user_input)
    return num_list

def find_max(num_list):
    max_num=num_list[0]
    for i in range(1,len(num_list)):
        if num_list[i] > max_num:
            max_num = num_list[i]
    return max_num

def find_min(num_list):
    min_num=num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] < min_num:
            min_num = num_list[i]
    return min_num

num_list=create_list()
print("Max number in the list : ",find_max(num_list))
print("Min number in the list : " , find_min(num_list))