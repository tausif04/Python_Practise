def extract_substring(input_string, start, end):
    return input_string[start:end]

user_string = input("Enter a string: ")

start_index = int(input("Enter the starting index: "))
end_index = int(input("Enter the ending index: "))
substring = extract_substring(user_string, start_index, end_index)
print("Extracted substring:", substring)