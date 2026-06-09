from book import Book
from coffee import Coffee

book_title = input("Enter book title: ")
book_pages = int(input("Enter page count: "))

book = Book(book_title, book_pages)

coffee_size = input("Enter coffee size (Small, Medium, Large): ")
coffee_price = float(input("Enter coffee price: "))

coffee = Coffee(coffee_size, coffee_price)

# Test Methods

print(f"\nBook: {book.title}")
print(f"Pages: {book.page_count}")
book.turn_page()

print(f"\nCoffee Size: {coffee.size}")
print(f"Price: ${coffee.price:.2f}")

coffee.tip()

print(f"New Price: ${coffee.price:.2f}")