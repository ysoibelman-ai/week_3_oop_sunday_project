from classes.book_class import Book

class Library():
    def __init__(self):
        self.library_books = []

    def add_book(self,book:Book):
        if isinstance (book,Book):
            self.library_books.append(book)
        else:
            raise ValueError ("book must be a Book Object")

    def available_books(self):
        available_books = []
        for book in self.library_books:
            if book.available > 0:
                available_books.append(book.name)
        return available_books