#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in ['small', 'medium', 'large']:
            self._size = value
        else:
            print("Size must be 'small', 'medium', or 'large'.")

    def tip(self):
        print("This coffee is great,heres a tip!")
        self.price += 1    