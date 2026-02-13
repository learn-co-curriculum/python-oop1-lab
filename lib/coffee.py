#!/usr/bin/env python3

class Coffee:
    size = "Medium"

    def __init__(self, size, price):
        if size not in ["Small", "Medium", "Large"]:
            return print("size must be 'Small', 'Medium', or 'Large'")
        self.size = size

        if not isinstance(price, (int, float)):
            return print("price must be a number")
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1