#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price  # triggers the setter

    # Property to ensure size is valid
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
            self._size = "Medium"  # default fallback
        else:
            self._size = value

    # Method to tip
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
