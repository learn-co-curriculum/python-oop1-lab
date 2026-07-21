#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price  # Standard attribute, can be modified by tip()

    @property
    def size(self):
        """Getter for coffee size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter to validate coffee size."""
        # Convert to title case to handle 'small' or 'SMALL' gracefully
        valid_sizes = ["Small", "Medium", "Large"]
        
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            return
            
        self._size = value

    def tip(self):
        """Prints a compliment and increases the coffee price by 1."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
