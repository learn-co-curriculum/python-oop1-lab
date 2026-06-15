# lib/coffee.py

class Coffee:
    """
    Represents a coffee sold in the bookstore.
    """

    def __init__(self, size, price):
        """
        Initialize a Coffee object.
        """
        self._size = None
        self._price = price
        self.size = size

    @property
    def size(self):
        """
        Getter for size.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Ensures size is Small, Medium, or Large.
        """
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def tip(self):
        """
        Adds a $1 tip to the coffee price.
        """
        print("This coffee is great, here’s a tip!")
        self._price += 1