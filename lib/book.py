#!/usr/bin/env python3

class Book:
    """
    Book class represents a book in the bookstore.
    Allows turning pages and validates page count.
    """

    def __init__(self, title, page_count):
        # Required attributes
        self.title = title
        self.page_count = page_count  # Uses property setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Ensure page_count is an integer
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        #Simulates turning a page.
        print("Flipping the page...wow, you read fast!")