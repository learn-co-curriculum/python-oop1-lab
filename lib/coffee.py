
#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Store the coffee's size and price.
        self.size = size
        self.price = price

    @property
    def size(self):
        # Return the current coffee size.
        return self._size

    @size.setter
    def size(self, value):
        # Accept only the three permitted coffee sizes.
        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Display the tip message and increase the price by one.
        print("This coffee is great, here’s a tip!")
        self.price += 1
