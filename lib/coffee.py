#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price):
        if size!="Small" or size!="Medium" or size!="Large":
            raise ValueError("size must be Small, Medium, or Large")
        
        self.size=size
        self.price=price

    def tip(self):
        print(f"This coffee is great, here’s a tip!")
        self.price+=1
        return self.price