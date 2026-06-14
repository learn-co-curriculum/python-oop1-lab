class Coffee:
    def __init__(self, size, price):
        # Call the setter to enforce value validation during initialization
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = None

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1