#!/usr/bin/env python3

class Coffee:
    
    """
    Represents a coffee sold in the bookstore.
    """

    def __init__(self, size, price):
        self.size = size  # validated by property
        self.price = price

    # Size property getter
    @property
    def size(self):
        return self._size

    # Size property setter with validation
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
    pass