class Book:
    """Book class representing a book in the bookstore"""
    
    def __init__(self, title, page_count):
        """
        Initialize a new Book instance
        
        Args:
            title (str): The title of the book
            page_count (int): The number of pages in the book
        """
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count of the book"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Set the page count with validation to ensure it's an integer
        
        Args:
            value: The page count value to set
            
        Prints error message if value is not an integer
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Simulate turning a page in the book"""
        print("Flipping the page...wow, you read fast!")