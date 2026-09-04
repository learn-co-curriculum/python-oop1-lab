#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
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

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1

if __name__ == "__main__":
    print("\n\n=== Creating a Coffee ===")
    coffee = Coffee(
        input("Enter the coffee size (Small, Medium, or Large): "),
        float(input("Enter the price: ")),
    )

    print(f"\nCoffee Size: {coffee.size}")
    print(f"Coffee Price : {coffee.price:.2f}")

    print("\n---- Adding a tip ---")
    coffee.tip()
    print(f"New price after a tip: {coffee.price:.2f}")

    print("\n--- Testing Coffee property validation ---")
    coffee.size = "Medium"
    print(f"Updated size: {coffee.size} ")

    coffee.size = "ExtraLarge"
    print(f"Size after invalid input : {coffee.size}")