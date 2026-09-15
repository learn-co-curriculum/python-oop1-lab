#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title=title

        if page_count is not int:
            raise ValueError("page_count must be an integer")
        self.page_count=page_count

    def turn_page(self):
        print(f"Flipping the page...wow, you read fast!")    