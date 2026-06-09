# Book class for the bookstore OOP lab

class Book:

    def __init__(self, title, page_count):
        # Store title directly
        self.title = title
        # Use property setter for validation
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Ensure page_count is an integer
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        # Simulate turning a page
        print("Flipping the page...wow, you read fast!")
