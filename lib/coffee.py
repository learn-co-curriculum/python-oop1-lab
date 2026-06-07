# lib/coffee.py
# Represents a Coffee object sold in the bookstore.


class Coffee:
    """Models a coffee drink available for purchase in the bookstore."""

    # Valid size options
    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        # Use property setters so validation runs on init
        self.size = size
        self.price = price

    # ── size property ─────────────────────────────────────────────────────────

    @property
    def size(self):
        """Return the size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """Ensure size is Small, Medium, or Large before storing it."""
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
            self._size = None
        else:
            self._size = value

    # ── price property ────────────────────────────────────────────────────────

    @property
    def price(self):
        """Return the current price of the coffee."""
        return self._price

    @price.setter
    def price(self, value):
        """Store the price value."""
        self._price = value

    # ── Methods ───────────────────────────────────────────────────────────────

    def tip(self):
        """
        Add a tip for the coffee.
        Prints a thank-you message and increases the price by 1.
        """
        print("This coffee is great, here's a tip!")
        self._price += 1

    # ── String representation ─────────────────────────────────────────────────

    def __repr__(self):
        return f"Coffee(size='{self.size}', price={self.price})"