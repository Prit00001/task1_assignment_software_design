class Library:

    def __init__(self):
        self.books={}

    def add_book(self,book_id,title):
        if book_id in self.books:
            raise ValueError("Duplicate Book Id")
        self.books[book_id]=title
        return True