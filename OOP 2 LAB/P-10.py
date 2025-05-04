def reverse_list():
        size=int(input("Enter the size of the list:"))
        num_list = []
        for i in range(size):
             user_input = input("Enter value for list: ")
             num_list.append(user_input)
        print("List in reverse order:", num_list[::-1])
reverse_list()
