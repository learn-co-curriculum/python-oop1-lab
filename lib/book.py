#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self.page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self.page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book1 = Book("And Then There Were None", 272)
print(book1.page_count)
book1.turn_page()
    
        