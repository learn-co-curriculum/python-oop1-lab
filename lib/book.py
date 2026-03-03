#!/usr/bin/env python3

class Book:
    """
    Represents a book in the bookstore.
    """

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # this will trigger the property setter

    # Property getter
    @property
    def page_count(self):
        return self._page_count

    # Property setter with validation
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    pass
    
        