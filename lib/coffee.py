#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price:int):
        self.size = size
        self.price = price
# Ensure size is either Small, Medium, or Large
# If not print “size must be Small, Medium, or Large”
        if self.size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1