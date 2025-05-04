import os
# Create a new directory
os.mkdir("new_directory")

# List all files and directories in the current directory
print(os.listdir("."))

## Create a file in the new directory and write to it
with open("new_directory/example.txt", "w") as file:
    file.write("Writing content to a file in a new directory.")

with open("new_directory/example.txt", "r") as file:
    data=file.read()
    print(data)

# Rename a directory
os.rename("new_directory", "renamed_directory")

# Remove a file inside the directory first
os.remove("renamed_directory/example.txt")
# Delete the directory
os.rmdir("renamed_directory")

