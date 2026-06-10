class Book:
    def __init__(self, title, page_count):
        self.title = title

        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            self._page_count = None

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")