
def search_tuple(tup, value):
    if value in tup:
        return f"Value '{value}' found in the tuple."
    else:
        return f"Value '{value}' not found in the tuple."


my_tuple = tuple(map(int, input("Enter the numbers for the tuple (separated by spaces): ").split()))
value =int( input("Enter the value to search: "))
result = search_tuple(my_tuple, value)
print(result)
