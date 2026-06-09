#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def price(self):
        return self._price
    
    @size.setter
    def size(self, value):
        if value in ["small", "medium", "large"]:
            self._size = value
        else:
            print("size must be 'small', 'medium', or 'large'")
            self._size = None
    
    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price +=1

    pass