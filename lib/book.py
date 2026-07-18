#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count): 
        self.title = title # instance property
        self.page_count = page_count # instance property

    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self.page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
