#!/usr/bin/env python3

class Book:
    def turn_page(self):
            print("Flipping the page...wow, you read fast!")

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count
        
    @page_count.setter
    def page_count(self, value):
        """page_count must be an integer"""

        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    pass