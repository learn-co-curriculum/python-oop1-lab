#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Initialize the coffee size using the validated property.
        self.size = size

        # Store the coffee price.
        self.price = price

    @property
    def size(self):
        # Return the current coffee size.
        return self._size

    @size.setter
    def size(self, value):
        # Accept only the three supported sizes.
        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Increase the price by 1 when the customer tips.
        print("This coffee is great, here’s a tip!")
        self.price += 1
