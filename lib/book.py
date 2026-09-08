#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        
        if not isinstance(page_count, int):
            raise TypeError("page_count must be an integer")
            
        self.page_count = page_count
                
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
