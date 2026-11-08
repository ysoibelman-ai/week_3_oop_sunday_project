from classes.book_class import Book
from classes.library_class import Library

def main():
    books = [
    Book("Clean Code", "Martin", 3),
    Book("Python Basics", "Cohen", 1),]
 
    books[0].borrow()
    books[1].borrow()
    
    try:
        books[1].borrow()
    except ValueError as error:
        print("Python Basics ->", error)
    
    try:
        Book("Empty", "Nobody", 0)
    except ValueError as error:
        print("Empty ->", error)
    
    for book in books:
        print(book, "| available:", book.is_available())
    
    print("Books in the library:", Book.total_books)

    library1 = Library()
    library1.add_book(books[0])
    print (library1.available_books())

if __name__ == "__main__":
    main()