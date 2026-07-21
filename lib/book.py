#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Getter property to retrieve the page count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Setter property to validate that the page count is an integer."""
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        """Method to simulate turning a page."""
        print("Flipping the page...wow, you read fast!")
       