#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    def get_size(self):
        return self._size
    def set_size(self, value):
        if type(value) is str and value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    size = property(get_size, set_size)

    def tip(self):
        self.price += 1
        print("This coffee is great, here's a tip!")
       

black= Coffee(size ="Large", price = 1.50)
print(black.size)
print(black.price)
'''says that the shoe has been repaired.'''
