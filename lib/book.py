class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        # Enforce that page_count is always an integer
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Simulates turning a page in the book
        print("Flipping the page...wow, you read fast!")