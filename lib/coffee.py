#!/usr/bin/env python3

class Coffee:
    # Initialize a Coffee object with a size and price
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only allow valid coffee sizes
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Increase the price by one dollar as a tip
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1