# Python OOP Lab: Bookstore

This project models a simple bookstore using Object-Oriented Programming
in Python. It includes two classes: `Book` and `Coffee`.

## Classes

### Book (`book.py`)
Represents a book with a title and page count.

- **Attributes:** `title`, `page_count` (validated as an integer)
- **Methods:** `turn_page()` — prints a message simulating turning a page

### Coffee (`lib/coffee.py`)
Represents a coffee sold in the store, with a size and price.

- **Attributes:** `size` (validated as "Small", "Medium", or "Large"), `price`
- **Methods:** `tip()` — prints a thank-you message and increases the price by 1

## Running the Tests

This project uses `pytest`. From the project root, run:

\`\`\`bash
python3 -m pytest tests/ -v
\`\`\`

All 7 tests should pass:

![Passing tests](![alt text](image.png))

