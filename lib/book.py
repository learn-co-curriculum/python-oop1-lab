#!/usr/bin/env python3

class Book:
    #Initialize object instance attributes(title and page count)
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count
    
    #Create get_page_count and set_page_count methods to controll page count property
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self,count):
        if not isinstance(count, int):
            print(f"page_count must be an integer")
        else:
            self._page_count = count
    #Create turn_page() method and print something
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    #page count property now controlled by get_size and set_size methods with Python's property()
    page_count = property(get_page_count, set_page_count)

#Test cases
""" title = input("Enter the book title: ")
page_count = input("Enter the book's page count: ")

book = Book(title,page_count)

print(book.turn_page()) """
        