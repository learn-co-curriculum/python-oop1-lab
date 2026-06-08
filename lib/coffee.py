#!/usr/bin/env python3

class Coffee:
    """Represents a coffee order with a size and price."""

    def __init__(self, size, price):
        # Store the validated size and the current price
        self._size = None
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Return the coffee size."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Validate coffee size and print an error for invalid values."""
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value
    
    def tip(self):
        """Simulate tipping for the coffee and increase its price."""
        print("This coffee is great, here's a tip!")
        self.price += 1
