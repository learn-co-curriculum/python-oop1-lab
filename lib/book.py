#!/usr/bin/env python3

class Book:
    def __init__(self, title=None, page_count=None):
        if title is None:
            title = input("Please enter the title of the book: ")
        if page_count is None:
            while True:
                val = input("Please enter the page count of the book: ")
                try:
                    page_count = int(val)
                    break
                except ValueError:
                    print("Page count must be an integer")

        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")