sizes = ["Small", "Medium", "Large"]


class Coffee:
    def __init__(self, size: str, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, str):
            print("Must be a string")
        elif size not in sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = size

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1