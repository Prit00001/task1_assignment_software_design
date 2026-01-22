class Library:

    def __init__(self):
        self.books={}

    def add_book(self,book_id,title):
        if book_id in self.books:
            raise ValueError("Duplicate Book Id")
        self.books[book_id] = {"title": title, "available": True}
        return True
    
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        if not self.books[book_id]["available"]:
            raise ValueError("Book already borrowed")
        
        self.books[book_id]["available"] = False
        return True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        self.books[book_id]["available"] = True
        return True