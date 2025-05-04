# Read Files Name From Directory and Print List
import os
os.mkdir("demo")

directory_path = "demo"
file_list = os.listdir(directory_path)
print(file_list)
print("Files in the directory:")
for file_name in file_list:
    print(file_name)