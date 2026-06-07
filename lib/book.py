# book.py
# This module defines the Book class for the python-oop1-lab project.

class Book:
    """Represents a book with a title and page count."""

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Turns to the next page of the book."""
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print(f"You have reached the last page ({self.page_count}) of '{self.title}'.")

    def __repr__(self):
        return f"Book(title='{self.title}', page_count={self.page_count})"