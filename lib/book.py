#!/usr/bin/env python3

class Book:
    #Initialize book object with required title and integer
    def __init__(self, title, page_count):
        self.title = title
        if isinstance(page_count, int):
            self.page_count = page_count
        else: print("page_count must be an integer")

    #turn_page method prints string
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    