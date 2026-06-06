# lib/coffee.py
# ─────────────────────────────────────────────
# Coffee Class — Bookstore OOP Lab
# ─────────────────────────────────────────────

class Coffee:
    """
    Represents a coffee object in the bookstore.

    Attributes:
        size  (str)   : The size of the coffee (Small, Medium, or Large).
        price (float) : The price of the coffee.
    """

    def __init__(self, size, price):
        """
        Constructor — runs automatically when a Coffee object is created.

        Args:
            size  (str)   : The coffee size.
            price (float) : The coffee price.
        """
        self.size = size    # uses the property setter below
        self.price = price  # store the price as an attribute

    # ── PROPERTY: size ────────────────────────
    @property
    def size(self):
        """Getter — returns the size value."""
        return self._size

    @size.setter
    def size(self, size):
        """
        Setter — validates that size is one of the
        accepted values: Small, Medium, or Large.
        """
        if size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = size

    # ── METHOD: tip() ─────────────────────────
    def tip(self):
        """
        Simulates tipping for the coffee.
        Prints a message and increases the price by 1.
        """
        print("This coffee is great, here's a tip!")
        self.price += 1  # increase price by 1

