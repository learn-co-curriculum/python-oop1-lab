#!/usr/bin/env python3
# Define a class named Coffee
class Coffee:
    # Constructor method initializing a Coffee instance with size and price attributes
    def __init__(self, size, price):
        self.size = size          # Set the size attribute
        self.price = price        # Set the price attribute

    # Method to add a tip to the price of the coffee and prints a message
    def tip(self):
        self.price += 1           # Increases the price attribute by 1
        print("This coffee is great, here’s a tip!")    

    # Define property getter for size
    @property
    def size(self):
        """The size property"""
        return self._size
        
    # define a setter for size property    
    @size.setter
    def size(self, value):
        """size must be Small, Medium, or Large"""
        # Check if value is one of the allowed sizes 
        if value in ("Small", "Medium", "Large"):
            self._size = value     # Set the _size attribute
        else:
        # If not, print an error message
            print("size must be Small, Medium, or Large")
    pass