cities_tuple =('Dhaka','Natore','Rajshahi','Bogura','Chattogram')
print("List of cities in the tuple:")
for city in cities_tuple:
    print(city)

cities_list = []

while True:
    print("\nWould you like to add a city to the list? (yes/no)")
    user_choice = input().lower()
    if user_choice == "yes":
         print("Enter the name of the city to add from the tuple:")
         city_name = input()
         if city_name in cities_tuple:
                 cities_list.append(city_name)
                 print(f"{city_name} has been added to the list.")
         else:
                print(f"{city_name} is not in the tuple.")
    elif user_choice == "no":
      break
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
print("\nFinal list of cities added:", cities_list)


