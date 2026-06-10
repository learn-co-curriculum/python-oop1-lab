#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Store title directly
        self.title = title

        # Validate page_count is an integer
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            self._page_count = 0  # fallback value

    # Property for page_count
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Method: turn page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        