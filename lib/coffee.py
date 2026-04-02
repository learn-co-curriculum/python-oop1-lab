#!/usr/bin/env python3

"""
__init__:
    size: Require user to input
    price: Require user to input
Properties:
    Size
        Ensure size is either Small, Medium, or Large
        If not print “size must be Small, Medium, or Large”
Methods:
    tip():
        Will print “This coffee is great, here's a tip!”
        Will increase price by 1 
"""

class Coffee:
    valid_sizes = ["Small", "Medium", "Large"]

    def __init__(self, size=None, price=None):
        if size is None:
            size = input("Please enter the size of the coffee (Small, Medium, Large): ")
        if price is None:
            while True:
                val = input("Please enter the price of the coffee: ")
                try:
                    price = float(val)
                    break
                except ValueError:
                    print("Price must be a number")
        
        self._size = None
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in self.valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here's a tip!")
        try:
            self.price = float(self.price) + 1
        except ValueError:
            self.price = 1.0

