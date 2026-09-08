#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        self.price = float(price)
        
        formatted_size = size.capitalize()
        if formatted_size not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
            self.size = None  
        else:
            self.size = formatted_size

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1.0
