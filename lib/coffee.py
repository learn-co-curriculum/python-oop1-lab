#!/usr/bin/env python3


class Coffee:
    """Models a coffee sold by the bookstore."""

    # Allowed coffee sizes.
    SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        # Size is validated via its property setter; price is stored directly.
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only accept one of the allowed sizes; otherwise warn the user.
        if value in Coffee.SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Leave a tip for the coffee and increase its price by 1."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
