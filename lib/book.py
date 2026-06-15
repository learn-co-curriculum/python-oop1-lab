# lib/book.py

class Book:
    """
    Represents a book sold in the bookstore.
    """

    def __init__(self, title, page_count):
        """
        Initialize a new Book object.

        Args:
            title (str): Title of the book
            page_count (int): Number of pages in the book
        """
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """
        Getter for page_count.
        """
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """
        Setter for page_count.

        Ensures page_count is an integer.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """
        Simulates turning a page.
        """
        print("Flipping the page...wow, you read fast!")