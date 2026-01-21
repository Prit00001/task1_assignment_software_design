import unittest
from src.library import Library

class TestLibrary(unittest.TestCase): # Capitalized 'L' for naming convention
    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        result = self.lib.add_book(111, "python basics")
        # Fixed typo: 'sel' to 'self'
        self.assertTrue(result)
        self.assertIn(111, self.lib.books)

    def test_add_duplicate_id_raises_error(self):
        # 1. Add the first book
        self.lib.add_book(111, "python basics")       
    
        # 2. Check for the error on the second add
        # Added missing colon and fixed indentation
        with self.assertRaises(ValueError):
            self.lib.add_book(111, "another topic")

if __name__ == "__main__":
    unittest.main()