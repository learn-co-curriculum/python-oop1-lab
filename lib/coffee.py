class Coffee:
    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        # Enforce that size is one of the allowed options
        if size in Coffee.VALID_SIZES:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Rewards good coffee with a $1 tip, added straight to the price
        print("This coffee is great, here’s a tip!")
        self.price += 1