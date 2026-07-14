#!/usr/bin/env python3

class Book:
    # Initialize a Book object with a title and page count
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Ensure page_count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")