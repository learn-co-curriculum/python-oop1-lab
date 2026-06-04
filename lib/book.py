#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if type(value) is int and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        self._page_count+=1
        print("Flipping the page...wow, you read fast!")

    page_count=property(get_page_count, set_page_count)

book1=Book("Book Title", 6)
print(book1.title, book1.page_count)
book1.turn_page()
print(book1.title, book1.page_count)

book2=Book("Book 2 Title", 8)
print(book2.title, book2.page_count)
book2.page_count="two"
print(book2.page_count)
        