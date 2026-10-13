#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Initialize the book's title.
        self.title = title

        # Store the page count using the validated property.
        self.page_count = page_count

    @property
    def page_count(self):
        # Return the current page count.
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Ensure the page count is an integer.
        if isinstance(value, int) and not isinstance(value, bool):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Simulate turning a page in the online book.
        print("Flipping the page...wow, you read fast!")
