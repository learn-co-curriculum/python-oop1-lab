#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
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
            print("Page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

title = input("Enter book title: ")
page_count = input("Enter page count: ")

try:
    page_count = int(page_count)
except ValueError:
    page_count = page_count

book = Book(title, page_count)

print(book.title)
book.turn_page()

        