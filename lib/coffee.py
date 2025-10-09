class Coffee:
    def __init__(self, size, price):
     
        self._size = None
        self._price = None

        self.size = size
        self.price = price

    @property
    def size(self):
        """Return coffee size."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Validate that size is one of the allowed options.
        If invalid, print an exact message.
        """
        allowed_sizes = {"Small", "Medium", "Large"}
        if value in allowed_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    @property
    def price(self):
        """Return coffee price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set coffee price without validation."""
        self._price = value

    def tip(self):
        """
        Print a message and increase price by 1.
        """
        import sys
        sys.stdout.write("This coffee is great, here’s a tip!\n")
        self._price += 1
