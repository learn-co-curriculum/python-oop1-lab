#!/usr/bin/env python3

class Coffee:
    """
    Coffee class represents a coffee item in the bookstore.
    Allows tipping and validates size.
    """

    def __init__(self, size, price):
        #Set required attributes
        self.size = size  # Uses property setter
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]

        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """
        Adds a tip to the coffee price.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1