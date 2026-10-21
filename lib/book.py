
#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Store the book's title and initialize its page count.
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        # Return the current page count.
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Only accept integer page counts.
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Display a message when the reader turns a page.
        print("Flipping the page...wow, you read fast!")
