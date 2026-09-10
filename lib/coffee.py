#!/usr/bin/env python3
class Coffee:
    def __init__(self, size, price):
        """Initialize a coffee with size and price"""
        self._size = None
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the coffee size"""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set size with validation"""
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        """Add a tip to the coffee price"""
        print("This coffee is great, here’s a tip!")
        self.price += 1
