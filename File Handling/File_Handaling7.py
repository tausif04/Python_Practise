#make list from csv file
import csv
csv_file_path="example.csv"

#Initialize an empty list to hold the rows
data_List=[]

#Reading the csv file and storing it in a list
with open(csv_file_path,mode='r') as file:
    csv_reader=csv.reader(file)

    #Iterate over each row in the csv file
    for row in csv_reader:
        data_List.append(row)

#Print the list
print(f"List from csv file:")
for eow in data_List:
    print(eow)