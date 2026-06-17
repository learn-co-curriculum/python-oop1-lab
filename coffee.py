# coffee.py
# Defines the Coffee class for the Bookstore application.

class Coffee:
    """A class to represent a coffee item available in the bookstore."""

    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1
