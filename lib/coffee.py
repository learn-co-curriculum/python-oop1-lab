# Coffee class - Represents a coffee in the bookstore

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    @property
    def size(self):
        # Getter for size
        return self._size
    
    @size.setter
    def size(self, value):
        # Setter ensures size is Small, Medium, or Large
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        # Adds a tip and increases price
        print("This coffee is great, here's a tip!")
        self.price += 1