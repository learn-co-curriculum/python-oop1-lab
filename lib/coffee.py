#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
       self.size = size #instance property
       self.price = price #instance property

    def size(self):
        return self.size
    
    def size(self, value):
        if value not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium or Large")
        else:
            self.size = value

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1

        