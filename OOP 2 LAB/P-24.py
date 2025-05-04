def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Look Up Employee Department")
    print("4. Exit")


def add_employee(employees):
    name = input("Enter the employee's name: ")
    department = input("Enter the employee's department: ")
    employees[name] = department
    print(f"Employee {name} added to department {department}.")


def remove_employee(employees):
    name = input("Enter the employee's name to remove: ")
    if name in employees:
        del employees[name]
        print(f"Employee {name} removed.")
    else:
        print(f"Employee {name} not found.")


def lookup_employee(employees):
    name = input("Enter the employee's name to look up: ")
    department = employees.get(name)
    if department:
        print(f"{name} works in the {department} department.")
    else:
        print(f"Employee {name} not found.")


employees = {}

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == '1':
            add_employee(employees)
    elif choice == '2':
            remove_employee(employees)
    elif choice == '3':
            lookup_employee(employees)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

