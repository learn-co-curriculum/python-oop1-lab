#!/usr/bin/env python3

class Book:
    def __init__(self,title = None,page_count = 0) :
        self.title = title
        self._page_count = page_count
       
    def get_page_count(self):
        return self._page_count
    def set_page_count(self,value):
        if isinstance(value,int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    def turn_page(self) : 
        print("Flipping the page...wow, you read fast!")
    page_count = property(get_page_count,set_page_count)

book1 = Book("book1",27)
book1.page_count = "200"
print(f"{book1.title},{book1.page_count}")
# book1.title = input("Enter the book title: ")
# book1.turn_page()