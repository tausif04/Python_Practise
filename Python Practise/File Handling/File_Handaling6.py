#Make CSV File Form List
import csv
# Data to write
data = [
["Name", "Salary", "Designation", "Department", "Location"],
["Alice", 70000, "Software Engineer", "IT", "New York"],
["Bob", 85000, "Data Scientist", "Data", "San Francisco"],
["Charlie", 60000, "System Administrator", "IT", "Chicago"],
["David", 95000, "Product Manager", "Product", "Boston"],
["Eve", 72000, "UX Designer", "Design", "Los Angeles"]
]

# Path to the csv file
csv_file_path="example.csv"

#writing to the csv file
with open(csv_file_path,mode='w',newline='') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully")