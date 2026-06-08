#!/usr/bin/env python3

class Book:
    """Represents a book with a title and page count."""

    def __init__(self, title, page_count):
        # Set the title directly and initialize the validated page count
        self.title = title
        self._page_count = None
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Return the current page count for the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Validate page_count and print an error if it is not an integer."""
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    
    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")
    
        