#!/usr/bin/env python3

class Coffee:
    def __init__(self):
        self.size = input("Enter coffee size (Small, Medium, Large): ")
        self.price = float(input("Enter coffee price: "))
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
        
coffee = Coffee()
coffee.tip()
print("New price:", coffee.price)        
    