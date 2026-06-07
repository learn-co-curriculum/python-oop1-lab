# Bookstore Application

A Python application that models a bookstore with two core objects: **Book** and **Coffee**.

---

## Features

### Book
- Create a book with a `title` and `page_count`
- Validates that `page_count` is an integer
- Call `turn_page()` to simulate reading

### Coffee
- Create a coffee with a `size` and `price`
- Validates that `size` is `Small`, `Medium`, or `Large`
- Call `tip()` to add a tip — increases price by 1

---

## Project Structure

```
bookstore/
├── lib/
│   ├── book.py          # Book class
│   └── coffee.py        # Coffee class
├── testing/
│   ├── book_test.py     # Tests for Book
│   └── coffee_test.py   # Tests for Coffee
└── README.md
```

---

## How to Run

### Run all tests
```bash
pytest testing/
```

### Run book tests only
```bash
pytest -x testing/book_test.py
```

### Run coffee tests only
```bash
pytest -x testing/coffee_test.py
```

---

## Example Usage

```python
from lib.book import Book
from lib.coffee import Coffee

# Book
book = Book("Python Crash Course", 544)
book.turn_page()
# → Flipping the page...wow, you read fast!

# Coffee
coffee = Coffee("Medium", 4.50)
coffee.tip()
# → This coffee is great, here's a tip!
print(coffee.price)
# → 5.50
```

---

## Author
Brian Kipchirchir