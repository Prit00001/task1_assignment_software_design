import unittest
from src.library import Library

class TestLibrary(unittest.TestCase): 
    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        result = self.lib.add_book(111, "python basics")
        
        self.assertTrue(result)
        self.assertIn(111, self.lib.books)

    def test_add_duplicate_id_raises_error(self):
        self.lib.add_book(111, "python basics")       
    
        with self.assertRaises(ValueError):
            self.lib.add_book(111, "another topic")



    def test_borrow_book_success(self):
        self.lib.add_book(222, "Success Story")
        result = self.lib.borrow_book(222)
        self.assertTrue(result)
        self.assertFalse(self.lib.books[222]["available"])

    def test_borrow_unavailable_book_error(self):
        self.lib.add_book(222, "Success Story")
        self.lib.borrow_book(222)  # First borrow
        
        with self.assertRaises(ValueError):
            self.lib.borrow_book(222)  # Double borrow should fail

    def test_return_book_updates_status(self):
        self.lib.add_book(333, "Return Test")
        self.lib.borrow_book(333)
        self.lib.return_book(333)
        self.assertTrue(self.lib.books[333]["available"])

if __name__ == "__main__":
    unittest.main()