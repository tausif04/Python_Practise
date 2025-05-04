with open("example.text", "w") as file:
    file.write("Writing new content to the file.")
#Rename the file
import os
os.rename("example.text","new_ex.text")

#reading the file and print it
with open("new_ex.text","r") as file:
    data=file.read()
print(data)

#Remove or delete any file
os.remove("new_ex.text")