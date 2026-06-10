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
        if value not in ("Small", "Medium", "Large"):
            raise ValueError("size must be Small, Medium, or Large")
        self._size = value

    def tip(self):
        print("This coffee is great,here's a tip!")

coffee = Coffee("Medium", 3.50)
coffee.tip()
print(coffee.price)
        