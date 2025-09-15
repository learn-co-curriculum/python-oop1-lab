#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count= page_count

    def get_pages(self):
        return self._page_count
    
    def set_pages(self, value):
        if type(value) is int and 0 <= value:
            self._page_count = value
        else:
            print("page_count must be an integer")
        
    page_count = property(get_pages, set_pages)

    def turn_page(self):
        if self.page_count > 0:
            self.page_count -= 1
        #print(f"Flipping the page {self.page_count+1}, wow, you read fast!")
        print("Flipping the page...wow, you read fast!")

# book1 = Book("1948", -5)
# book2 = Book("Harry Potter", 100)
# print(book2.title)
# print(book2.page_count)
# book2.turn_page()
# book2.turn_page()
# print(book2.page_count)

    # pass
    
        