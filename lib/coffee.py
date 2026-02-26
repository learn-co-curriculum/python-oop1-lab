#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    def get_size(self):
        return self._size 
    
    def set_size(self, size):
        if size != "Small" and size != "Medium" and size != "Large":
            print("size must be Small, Medium, or Large")
        
        else:
            self._size = size
        
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
            
    size = property(get_size, set_size)
    
coffee = Coffee("Extra Large", 2.50)