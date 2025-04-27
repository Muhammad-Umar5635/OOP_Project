class Book:
    total_books = 0  # Class variable shared by all instances

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
Book("Umar")
Book("1984")
Book("3 Idiots")
print("Total numbers of Books: ",Book.total_books)
