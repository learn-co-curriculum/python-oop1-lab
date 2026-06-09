# Coffee class for the bookstore OOP lab

class Coffee:

    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        # Use property setter for validation
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Ensure size is one of the valid options
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        # Print tip message and increase price by 1
        print("This coffee is great, here's a tip!")
        self.price += 1
