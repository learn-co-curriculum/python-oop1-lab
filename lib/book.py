class Book:
    def __init__(self, title, page_count):
        self.title = title
        # Call the setter to enforce type validation during initialization
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            # Setting it to None or keeping it unassigned prevents invalid types
            self._page_count = None 

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")