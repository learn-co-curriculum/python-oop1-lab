
    # lib/book.py
# ─────────────────────────────────────────────
# Book Class — Bookstore OOP Lab
# ─────────────────────────────────────────────

class Book:
    """
    Represents a book object in the bookstore.

    Attributes:
        title (str)      : The title of the book.
        page_count (int) : The number of pages in the book.
    """

    def __init__(self, title, page_count):
        """
        Constructor — runs automatically when a Book object is created.

        Args:
            title (str)      : The book's title.
            page_count (int) : The number of pages.
        """
        self.title = title          # store the title as an attribute
        self.page_count = page_count  # uses the property setter below

    # ── PROPERTY: page_count ──────────────────
    @property
    def page_count(self):
        """Getter — returns the page count value."""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Setter — validates that page_count is an integer
        before storing it.
        """
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    # ── METHOD: turn_page() ───────────────────
    def turn_page(self):
        """Simulates turning a page of the book."""
        print("Flipping the page...wow, you read fast!")
        