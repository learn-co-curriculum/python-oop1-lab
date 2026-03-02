#!/usr/bin/env python3

class Coffee:
    #Initialize object instance attributes(size and price)
    def __init__(self,size,price):
        self.size = size
        self.price = price

    #Create get_size and set_size methods to controll size property
    def get_size(self):
        return self._size
    
    def set_size(self, size_input):
        if size_input == "Small" or size_input == "Medium" or size_input=="Large":
            self._size = size_input
        else:
            print("size must be Small, Medium, or Large")
    
    #Create tip() method to add 1 to coffee price
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1
        return self.price

    #Size property controlled by get_size and set_size methods
    size = property(get_size,set_size)

#Test cases
""" size = input("Enter the coffee size: ")
price = input("Enter the coffee price: ")

coffee = Coffee(size,int(price))

print(coffee.tip()) """