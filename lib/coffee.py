class Coffee:
    """
    The Coffee class models a coffee item in a bookstore café.

    Each Coffee object has:
    - a size (Small, Medium, or Large)
    - a price (a number)

    It also supports tipping, which increases the price.
    """

    def __init__(self, size, price):
        """
        The constructor method.

        This method runs automatically when a new Coffee object is created.
        It initializes the size and price attributes.

        Parameters:
        size (str): The size of the coffee
        price (float or int): The price of the coffee
        """
        self.size = size     # This uses the size setter below
        self.price = price   # Stores the price directly

    # ---------- SIZE PROPERTY ----------

    @property
    def size(self):
        """
        Getter method for size.

        This allows us to access the coffee's size using:
        coffee.size
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        This runs whenever we try to set coffee.size.
        It ensures the size is one of the allowed values.
        """
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    # ---------- TIP METHOD ----------

    def tip(self):
        """
        Adds a tip to the coffee.

        This method:
        1. Prints a friendly message
        2. Increases the coffee's price by 1
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1
##The code above defines a Coffee class with a constructor that initializes the size and price of the coffee. It includes a property for size with a getter and setter to ensure valid sizes, and a method to add a tip that increases the price by 1.