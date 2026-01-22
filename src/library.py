class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title):
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
    
  def generate_report(self):
        # Indent these lines by 4 spaces (one tab) inside the function
        report_lines = ["Book ID | Title | Status"]
        for book_id, info in self.books.items():
            status = "Available" if info["available"] else "Borrowed"
            report_lines.append(f"{book_id} | {info['title']} | {status}")
        return "\n".join(report_lines)