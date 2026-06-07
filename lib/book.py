# lib/book.py
# Represents a Book object in the bookstore application.


class Book:
    """Models a book available for reading in the bookstore."""

    def __init__(self, title, page_count):
        # Store title directly - no special validation required
        self.title = title
        # Use the property setter so validation runs on init
        self.page_count = page_count

    # ── page_count property ───────────────────────────────────────────────────

    @property
    def page_count(self):
        """Return the page count of the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Ensure page_count is an integer before storing it."""
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = None
        else:
            self._page_count = value

    # ── Methods ───────────────────────────────────────────────────────────────

    def turn_page(self):
        """Simulate turning a page of the book."""
        print("Flipping the page...wow, you read fast!")

    # ── String representation ─────────────────────────────────────────────────

    def __repr__(self):
        return f"Book(title='{self.title}', page_count={self.page_count})"