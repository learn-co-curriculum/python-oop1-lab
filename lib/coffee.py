
class Coffee:
    """Represents a coffee with size and price, allowing tipping."""

    VALID_SIZES = {"Small", "Medium", "Large"}

    def __init__(self, size: str, price: float):
        self._price = price
        self.size = size  # Triggers setter validation

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
            self._size = "Medium"
        else:
            self._size = value

    @property
    def price(self) -> float:
        return self._price

    def tip(self):
        """Add a tip to the coffee price."""
        print("This coffee is great, here's a tip!")
        self._price += 1