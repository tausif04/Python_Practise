def calculate_ticket_price(age, show_time):

    if age <= 0:
        return "Invalid input. Age must be a positive integer."


    if not (0 <= show_time < 2400 and show_time % 100 < 60):
        return "Invalid input. Please provide the showtime in the correct format."


    if age <= 10:
        price = 300
    elif 11 <= age <= 25:
        price = 500
    elif 26 <= age <= 60:
        price = 800
    else:
        price = 400

    discount = 0.0
    if show_time < 1700:
        discount = price * 0.10


    discounted_price = price - discount


    result = f"Ticket price: {price} BDT\nDiscount: {discount:.2f} BDT\nDiscounted price: {discounted_price:.2f} BDT"
    return result

age = int(input("Age: "))
show_time = int(input("Showtime (HHMM): "))

print(calculate_ticket_price(age, show_time))