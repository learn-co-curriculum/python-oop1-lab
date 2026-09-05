#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.price = price
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
