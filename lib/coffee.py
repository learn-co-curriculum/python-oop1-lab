#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")    

    @property
    def size(self):
        """The size property"""
        return self._size
        
    @size.setter
    def size(self, value):
        """size must be Small, Medium, or Large"""

        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    pass