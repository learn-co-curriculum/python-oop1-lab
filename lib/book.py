# Book class - Represents a book in the bookstore

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        # Getter for page_count
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        # Setter ensures page_count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        # Simulates turning a page
        print("Flipping the page...wow, you read fast!")