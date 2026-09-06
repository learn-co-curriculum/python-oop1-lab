#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        """Initialize a book with title and page_count"""
        self.title = title
        self._page_count = None
        self.page_count = page_count  # Use setter for validation
    
    @property
    def page_count(self):
        """Get the page count"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Set page count with validation"""
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Print a message when turning the page"""
        print("Flipping the page...wow, you read fast!")
