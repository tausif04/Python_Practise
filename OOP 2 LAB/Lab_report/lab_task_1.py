class Book:
    total_books = 0  
    
    def __init__(self, title, author, is_available=True):  
        self.title = title
        self.author = author
        self.is_available = is_available
        Book.total_books += 1  

    def display(self):
        availability = "available" if self.is_available else "not available"  
        print(f"Title: {self.title}, Author: {self.author}, Availability: {availability}")
    
    def borrowed(self):
        if self.is_available:
            self.is_available = False
            print("The book is borrowed by you.")
        else:
            print("The book is not available for borrowing.")


book1 = Book("Alibaba", "Ostad Jakir", True)
book1.display()  
book1.borrowed()  
book1.display()  
