#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Validate size input
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")
            self._size = "Small"  # default fallback

        self.price = price

    # Property for size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Method: tip coffee
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1