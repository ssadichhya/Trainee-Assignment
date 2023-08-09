class book:
    def __init__(self,Title,Author,ISBN,Genre,Availability=True):
        self.Author=Author
        self.Title=Title
        self.ISBN=ISBN
        self.Genre=Genre
        self.Availability=Availability

    def __str__(self):
        return(f'Author Name:{self.Author}, Title:{self.Title}, ISBN: {self.ISBN},Genre:{self.Genre},Availability:{self.Availability}')



class LibraryCatalog:
    def __init__(self):
        self.books=[]

    def add_book(self,book_obj):
        self.books.append(book_obj)
        
    def get_book_details(self, isbn):
        for book in self.books:
            if book.ISBN == isbn:
                return book
        return ("Not found")

    def borrow_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN and book.Availability:
                book.Availability = False
                return ('Book Borrowed')
        return ('Book not available')


book_1=book("harry potter", "jk","1234","fantasy")
book_2=book("lord of the rings", "tolkein","127734","fantasy")

catalog=LibraryCatalog()
lc1=catalog.add_book(book_1)
lc2=catalog.add_book(book_2)

print(catalog.borrow_book("1234"))

print(catalog.get_book_details("1234"))
