# coffee.py
# This module defines the Coffee class for the python-oop1-lab project.

class Coffee:
    """Represents a coffee order with a size and price."""

    def __init__(self, size, price):
        self.size = size
        self.price = price
        self.tip_amount = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value
def tip(self, amount=0):
    self.tip_amount += amount
    print("This coffee is great, here\u2019s a tip!")

    def total(self):
        return self.price + self.tip_amount

    def __repr__(self):
        return f"Coffee(size='{self.size}', price={self.price})"
