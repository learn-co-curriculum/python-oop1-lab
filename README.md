# Object Oriented Programming Lab - Bookstore

## Description

This project demonstrates the fundamentals of Object-Oriented Programming (OOP) in Python by modeling a bookstore. The application contains two classes:

* **Book** – Represents a book in the bookstore and allows users to turn pages.
* **Coffee** – Represents a coffee item sold in the bookstore and allows users to leave a tip.

The project was developed using a test-driven approach and includes validation for object properties.

---

## Features

### Book Class

Attributes:

* `title`
* `page_count`

Methods:

* `turn_page()`

  * Displays the message:

  ```
  Flipping the page...wow, you read fast!
  ```

Validation:

* `page_count` must be an integer.
* If an invalid value is provided, the program prints:

  ```
  page_count must be an integer
  ```

---

### Coffee Class

Attributes:

* `size`
* `price`

Methods:

* `tip()`

  * Displays the message:

  ```
  This coffee is great, here’s a tip!
  ```

  * Increases the coffee price by 1.

Validation:

* `size` must be one of:

  * Small
  * Medium
  * Large

* If an invalid size is provided, the program prints:

  ```
  size must be Small, Medium, or Large
  ```

---

## Project Structure

```text
.
├── lib
│   ├── book.py
│   └── coffee.py
├── testing
│   ├── book_test.py
│   └── coffee_test.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone git@github.com:penzimbuthia-sudo/oop-p2-cash-register-lab.git
```

2. Navigate to the project directory:

```bash
cd python-oop1-lab
```

3. Install dependencies:

```bash
pipenv install
```

4. Activate the virtual environment:

```bash
pipenv shell
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run Book tests only:

```bash
pytest -x testing/book_test.py
```

Run Coffee tests only:

```bash
pytest -x testing/coffee_test.py
```

---

## Example Usage

### Book

```python
from lib.book import Book

book = Book("And Then There Were None", 272)
book.turn_page()
```

Output:

```text
Flipping the page...wow, you read fast!
```

### Coffee

```python
from lib.coffee import Coffee

coffee = Coffee("Large", 3.50)
coffee.tip()

print(coffee.price)
```

Output:

```text
This coffee is great, here’s a tip!
4.5
```

---

## Author

Created as part of the Object-Oriented Programming (OOP) Lab - Bookstore assignment.