#!/usr/bin/env python3
# Define a class named Book
class Book:
    # Method simulating turning a page in the book
    def turn_page(self):
            print("Flipping the page...wow, you read fast!")
    # Constructor method initializing a Book instance with a title and page count
    def __init__(self, title, page_count):
        self.title = title             # Set title attribute 
        self.page_count = page_count   # Set page_count attribute

    #  Define property getter for page_count    
    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count        # Return the page_count attribute
    
    # Define a setter for the page_count property
    @page_count.setter
    def page_count(self, value):
        """page_count must be an integer"""
        # Checks if value is an integer
        if isinstance(value, int):
            self._page_count = value   # If value is an integer, set the page_count attribute
        else:
        # If value is not an integer, print an error message
            print("page_count must be an integer")
    pass