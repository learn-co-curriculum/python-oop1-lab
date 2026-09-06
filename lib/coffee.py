class Coffee:
    def __init__(self, size, price):
        self._size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Validation logic required by the test
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            # The test specifically looks for this print statement
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Make sure to use the curly apostrophe ’ to match the test
        print("This coffee is great, here’s a tip!")
        # test_tip_adds_to_price requires adding 1 to the price
        self.price += 1.0