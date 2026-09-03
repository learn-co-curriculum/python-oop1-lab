#!/usr/bin/env python3


class Coffee:
    def __init__(self, size, price):
        # Initialize coffee attributes
        self.size = size
        self.price = price

    @property
    def size(self):
        # Getter for size
        return self._size

    @size.setter
    def size(self, value):
        # Validate that size is one of the allowed options
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Print thank you message and increase the price by 1
        print("This coffee is great, here’s a tip!")
        self.price += 1.0