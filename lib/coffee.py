#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

        if size != "Small" or size != "Medium" or size != "Large":
            print("size must be Small, Medium or Large")

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1
        print(self.price)
