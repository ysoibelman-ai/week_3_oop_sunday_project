from book_class import Book
class Library():
    def __init__(self):
        self.library_books = []

    def add_book(self):
        book_name = "Enter book name"
        book_author = "Enter book author"
        book_copies = "Enter anmount of copies"
        self.library_books.append(Book(book_name,book_author,book_copies))

    def available_books(self):
        self.available_books = []
        for book in self.library_books:
            if book.available > 0:
                self.available_books.append(book.name)
        return self.available_books