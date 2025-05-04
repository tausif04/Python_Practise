class Movie:
    total_movies = 0  

    def __init__(self, name="Untitled", genre="General", duration=0):
        self.name = name
        self.genre = genre
        self.duration = duration
        Movie.total_movies += 1

    @classmethod
    def default_movie(cls):
        """Alternate constructor with default movie details"""
        return cls(name="Default Movie", genre="Drama", duration=120)

    def display(self):
        return f"Movie: {self.name}, Genre: {self.genre}, Duration: {self.duration} mins"

class Schedule(Movie):
    def __init__(self, name, genre, duration):
        super().__init__(name, genre, duration)
        self.showtimes = []  
        self.seat_capacity = 100 

    def add_showtime(self, time, hall_number):
        """Add a showtime if it doesn't already exist"""
        if (time, hall_number) not in self.showtimes:
            self.showtimes.append((time, hall_number))

    def display(self):
        showtimes_details = ", ".join([f"{time} (Hall: {hall})" for time, hall in self.showtimes])
        return f"{super().display()}, Showtimes: [{showtimes_details}]"

class Booking(Schedule):
    def __init__(self, name, genre, duration):
        super().__init__(name, genre, duration)
        self.reservations = []  
        self.total_earnings = 0
        self.ticket_price = 10 

    def book_ticket(self, showtime, seats):
        """Book tickets for a showtime if seats are available"""
        available_seats = self.check_availability(showtime)
        if available_seats >= seats:
            self.reservations.append((self.name, showtime, seats))
            self.total_earnings += seats * self.ticket_price
            print(f"Successfully booked {seats} seat(s) for {self.name} at {showtime}.")
        else:
            print(f"Booking failed. Only {available_seats} seat(s) available.")

    def check_availability(self, showtime):
        """Check the number of seats available for a given showtime"""
        booked_seats = sum(seats for movie, stime, seats in self.reservations if stime == showtime and movie == self.name)
        return self.seat_capacity - booked_seats

    def calculate_earnings(self):
        """Calculate and return the total earnings for the movie"""
        return self.total_earnings

    def display(self):
        bookings_details = "\n".join([f"{movie} at {stime}, Seats: {seats}" for movie, stime, seats in self.reservations])
        return f"{super().display()}, Reservations:\n{bookings_details}\nTotal Earnings: ${self.total_earnings}"

if __name__ == "__main__":

    movie1 = Booking("Inception", "Sci-Fi", 148)
    movie2 = Booking("The Godfather", "Crime", 175)

    movie1.add_showtime("2:00 PM", 1)
    movie1.add_showtime("6:00 PM", 2)
    movie2.add_showtime("3:00 PM", 3)
    movie2.add_showtime("7:00 PM", 4)

    movie1.book_ticket("2:00 PM", 50)
    movie1.book_ticket("6:00 PM", 30)
    movie2.book_ticket("3:00 PM", 20)
    movie2.book_ticket("7:00 PM", 80)

    print("-- Movie Schedules --")
    print(movie1.display())
    print(movie2.display())

    print(f"\nTotal Movies Playing: {Movie.total_movies}")
