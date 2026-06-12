class Book:
    """Represents a book with title and page count, allowing page turning."""

    def __init__(self, title: str, page_count: int):
        self._title = title
        self.page_count = page_count  # Triggers setter validation

    @property
    def title(self) -> str:
        return self._title

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = 0
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")
