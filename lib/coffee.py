#!/usr/bin/env python3
coffee_sizes={"Small","Medium","Large"}

class Coffee:
    def __init__(self, size, price):
        self.size=size
        self.price=price
    
    #size GETTER AND SETTER
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, coff_size):
        if isinstance(coff_size, (str)) and coff_size in coffee_sizes:
            self._size=coff_size
        else:    
            print( "size must be Small, Medium, or Large")

    #price GETTER AND SETTER
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, amount):
        if isinstance(amount, (int, float)) and amount>0:
            self._price=amount
        else:    
            print("something over here")

    #ADDING TIP METHOD
    def tip(self, amount=1):
        if type(amount) is int and amount>0:
            print("This coffee is great, here’s a tip!")
            self._price+=amount
        else:
            print("Invalid amount")

#CREATING FIRST OBJECT
coffee1=Coffee("Medium", 33) 
print(coffee1.size, coffee1.price)

#CREATING SECOND OBJECT
coffee2= Coffee("Large", 67)
print(coffee2.size, coffee2.price)

print(setattr(coffee2, "size", "Largest"))

#TEST THE TIP 
coffee2.tip = 30
print(coffee2.price)

    