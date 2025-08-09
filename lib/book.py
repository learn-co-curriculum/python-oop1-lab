#!/usr/bin/env python3
# Represents a book with a title and page count
class Book:
    def __init__(self, title, page_count):
 # Set the title and page count using property setters
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            print("title must be a string")

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
    # Validate that page_count is an integer before assigning
        if isinstance(value, int):
            self._page_count = value

        else:
            print("page_count must be an integer")


    def turn_page(self):
    # Simulates turning a page in the book
        print("Flipping the page...wow, you read fast!")

    