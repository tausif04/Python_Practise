#Pyramid Printing Using For Loop

row=int(input("Enter the number of rows: "))

for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()


#Triangle printing Using for loop
for i in range(row):
    for j in range(i+1):
        print("#",end=" ")
    print()

#Reversed Pyramid Printing Using For Loop

for i in range(row):
    for j in range(i):
        print(" ",end="")
    for k in range(row-i):
        print("*",end=" ")
    print()

#Reversed Triangle Printing Using For Loop

for i in range(row):
    for j in range(row-i):
        print("#",end=" ")
    print()