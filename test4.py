class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print("You have borrowed", self.title,"by", self.author)
    def return_book(self):
        self.is_borrowed = False
        print("You have returned", self.title,"by", self.author)

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Just Mercy", "Bryan Stevenson")
book3 = Book("Dog Man", "Dav Pilkey")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()