

# Object Oriented Programming (OOP) - Bookstore Lab

## Overview

This project demonstrates Object-Oriented Programming (OOP) in Python by modeling a simple bookstore system. It includes two core classes: `Book` and `Coffee`.

The application focuses on class design, encapsulation, data validation using properties, and method behavior that modifies object state.

---

## Learning Objectives

This project demonstrates:

* Creating Python classes to model real-world objects
* Using attributes and methods to define object behavior
* Implementing property setters for data validation
* Applying encapsulation principles
* Writing methods that modify object state
* Using test-driven development (TDD) with pytest

---

## Project Structure

```text
lib/
├── book.py
└── coffee.py

testing/
├── book_test.py
└── coffee_test.py
```

---

## Features

---

### 📖 Book Class

The `Book` class represents a book with a title and page count.

#### Attributes:

* `title` (string): The name of the book
* `page_count` (int): The number of pages in the book

#### Behavior:

* Ensures `page_count` is an integer
* Stores book metadata

#### Methods:

##### `turn_page()`

Simulates turning a page in the book.

**Output:**

```text
Flipping the page...wow, you read fast!
```

#### Validation:

If `page_count` is not an integer:

```text
page_count must be an integer
```

---

### ☕ Coffee Class

The `Coffee` class represents a coffee order with size and price.

#### Attributes:

* `size` (string): Must be `"Small"`, `"Medium"`, or `"Large"`
* `price` (float): The price of the coffee

#### Methods:

##### `tip()`

Adds a tip to the coffee order.

**Behavior:**

* Prints a message
* Increases price by 1

**Output:**

```text
This coffee is great, here’s a tip!
```

#### Validation:

If size is invalid:

```text
size must be Small, Medium, or Large
```

---

## Testing

This project uses **pytest** for test-driven development.

Run all tests:

```bash
pytest -x
```

Run individual test files:

```bash
pytest -x testing/book_test.py
pytest -x testing/coffee_test.py
```

---

## Expected Output

```text
7 passed
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Property Decorators
* Encapsulation
* Pytest
* Test-Driven Development (TDD)

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd python-oop1-lab
```

Install dependencies:

```bash
pipenv install
```

Activate virtual environment:

```bash
pipenv shell
```

---

## Screenshot

Add a screenshot showing all tests passing:

```md
![Passing Tests](passed%207.png)
```

---

## Author

Vincent

---

## Summary

This project demonstrates how to model real-world objects using Python classes, enforce validation rules, and apply test-driven development to ensure correctness.

---




# trigger codegrade rerun
