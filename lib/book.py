#!/usr/bin/env python3

#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # triggers setter

    # Property to ensure page_count is an integer
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = 0  # default fallback
        else:
            self._page_count = value

    # Method to turn a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
