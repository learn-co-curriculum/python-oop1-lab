#!/usr/bin/env python3

class Coffee:
    """Coffee class representing a coffee beverage in the bookstore"""
    
    # Class constant for valid coffee sizes
    VALID_SIZES = ["Small", "Medium", "Large"]
    
    def __init__(self, size, price):
        """
        Initialize a new Coffee instance
        
        Args:
            size (str): The size of the coffee (Small, Medium, or Large)
            price (float): The price of the coffee
        """
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the size of the coffee"""
        return self._size
    
    @size.setter
    def size(self, value):
        """
        Set the coffee size with validation
        
        Args:
            value (str): The size value to set
            
        Prints error message if size is not Small, Medium, or Large
        """
        if value in self.VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    @property
    def price(self):
        """Get the price of the coffee"""
        return self._price
    
    @price.setter
    def price(self, value):
        """
        Set the coffee price
        
        Args:
            value (float): The price value to set
        """
        self._price = value
    
    def tip(self):
        """
        Add a tip to the coffee price
        
        Prints a thank you message and increases price by 1
        """
        print("This coffee is great, here's a tip!")
        self.price += 1