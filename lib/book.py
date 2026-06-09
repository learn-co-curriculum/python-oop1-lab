#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_Count):
        self.title = title
        self.page_Count = page_Count

    @property
    def page_count(self):
        return self.page_Count

    @page_count.setter
    def page_count(self, new_page_count):
        if type(new_page_count) == int:
            self.page_Count = new_page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        return "Flipping the page...wow, you read fast!"
    
    
        