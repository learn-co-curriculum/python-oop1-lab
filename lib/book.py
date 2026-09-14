class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, count):
        if not isinstance(count, int):
            print("page_count must be an integer")
        elif count <= 0:
            print("Pages must be greater than 0")
        else:
            self._page_count = count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")