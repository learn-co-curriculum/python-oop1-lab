#!/usr/bin/env python3


class Book:
    """Models an online book that can be read in the bookstore."""

    def __init__(self, title, page_count):
        # Title is stored as-is; page_count is validated via its property setter.
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Only accept integer page counts; otherwise warn the user.
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Simulate turning a page of the book."""
        print("Flipping the page...wow, you read fast!")
