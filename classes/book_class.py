class Book():
    total_books = 0

    def __init__(self,name,author,copies):
        if copies < 1:
            raise ValueError  ("copies must have at least 1")
        
        self.name = name
        self.author = author
        self.copies = copies
        self.available = copies
        Book.total_books += 1

    def __str__(self):
        return f"NAME: {self.name} | AUTHOR: {self.author} AVAILABLE BOOKS: {self.available} out of {self.copies}"

    def borrow (self):
        if self.available == 0:
            raise ValueError ("no copies available")
        else:
            self.available -= 1

    def return_book(self):
        if self.available == self.copies:
            raise ValueError ("all copies are already in")
        else:
            self.available +=1

    def is_available(self):
        if self.available:
            return True
        else:
            return False

print ()