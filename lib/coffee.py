#!/usr/bin/env python3

class Coffee:
    COFFEE_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self.size = size
        self.price = price
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1

    def get_size(self):
        return self._size
    def set_size(self, value):
        if value not in Coffee.COFFEE_SIZES:
            print("size must be Small, Medium, or Large")
            self._size = "Medium" 
        else: 
            self._size = value
    
    size = property(get_size, set_size)









    