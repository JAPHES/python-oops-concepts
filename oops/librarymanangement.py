# Book class with data abstraction and encapsulation
class Book:
    def __init__(self, title, author):
        self.__title = title # private attribute
        self.__author = author # private attribute
        self.__available = True # private attribute for availability

    # public methods to access private attributes
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

# Library class with encapsulation and inheritance
class Library:
    def __init__(self):
        self.__books = [] # private list of books

    def add_book(self, book):
        self.__books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.__books:
            if book.is_available():
                print(f"{book.get_title()} by {book.get_author()}")

    def borrow_book(self, title):
        for book in self.__books:
            if book.get_title() == title and book.is_available():
                if book.borrow():
                    print(f"You borrowed '{title}. Enjoy reading!")
                    return True
        print(f"'{title}' is not available.")
        return False
    def return_book(self, title):
        for book in self.__books:
            if book.get_title() == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned. Thankyou!")
                return True
        print(f"{title}' was not borrowed from the library.")
        return False

# User class

class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, library, title):
        print(f"{self.name} is attempting to borrow '{title}'...")
        library.borrow_book(title)

    def return_book(self, library, title):
        print(f"{self.name} is returning '{title}'...")
        library.return_book(title)



# Test the system
# Create library and add books

library = Library()
book1 = Book("The great gatsby", "F.Scott Fitzgerald")
book2 = Book("To kill a mockingbird", "Happer Lee")
book3 = Book("Pride and Prejudice", "Jane Austene")
book4 = Book("Moby-Dick", "Scott")
book5 = Book("1984", "Dick")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# create a user
user1 = User("JAPHES")
user2 = User("John")



# interact with the library

library.display_books()
user1.borrow_book(library,"The great gatsby")
user2.borrow_book(library,"Moby-Dick")
library.display_books()
user1.return_book(library, "The great gatsby")
user2.return_book(library, "Moby-Dick")
library.display_books()


