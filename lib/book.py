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
        if not isinstance(value, int):
            raise ValueError("page_count must be an integer")
        self._page_count = value
         
    def turn_page(self):
        print("Flipping the page...wow, you read fast")

book = Book("And Then There Were None", 272)
book.turn_page()

        


        
    
        