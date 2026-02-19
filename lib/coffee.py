#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Use setter so size is validated on creation too
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only allow these three specific sizes
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        # Print thank you message and add $1 to the price
        print("This coffee is great, here’s a tip!")
        self.price += 1