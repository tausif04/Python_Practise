def display_menu():
    print("\nMenu:")
    print("1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Exit")
elements = []
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter an element to add: ")
        elements.append(item)
        print(f"'{item}' has been added to the list.")

    elif choice == '2':
        if elements:
            item = input("Enter an element to remove: ")
            if item in elements:
                elements.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        else:
            print("The list is empty.")

    elif choice == '3':
        if elements:
            print("\nCurrent list of elements:")
            for idx, element in enumerate(elements, 1):
                print(f"{idx}. {element}")
        else:
            print("The list is empty.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")



