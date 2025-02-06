#Creating a file
with open("demo.text","w") as file:
    file.write("Hello, World!")#write in the file


# Read the content of a file
with open("demo.text", "r") as file:
    content = file.read()
    print(content)