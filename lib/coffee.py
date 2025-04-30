#!/usr/bin/env python3

class Coffee:
    #Initialize Coffe with required size and price 
    def __init__(self, size, price):
        if size in ["Small", "Medium", "Large"]:
            self.size = size
        else:
            print("size must be Small, Medium, or Large")
        self.price = price

    #Tip method will add 1 to the price
        def tip(self):
            print("This coffee is great, here's a tip!")
            self.price += 1
        