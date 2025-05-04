def tuple_to_list(t):
    return list(t)

my_tuple = (1, 'Hello', 3.14, True, [5, 6, 7])
my_list = tuple_to_list(my_tuple)

for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")
