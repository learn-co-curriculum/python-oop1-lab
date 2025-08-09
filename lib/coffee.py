#!/usr/bin/env python3

class Coffee:
    def __init__(self,size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size in ["Small","Medium","Large"]:
             self._size = size

        else:
            print("size must be Small, Medium, or Large")

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, (float, int)):
             self._price = price

        else:
            print("missing money")

    def tip(self):
        print('This coffee is great, here’s a tip!')
        self._price += 1
