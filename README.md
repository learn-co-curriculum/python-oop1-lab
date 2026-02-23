# Bookstore Model

This project models a simple bookstore using Object-Oriented Programming in Python.

## Features

### Book Class
- Requires title and page_count
- Validates page_count must be an integer
- Allows turning a page

### Coffee Class
- Requires size and price
- Validates size must be Small, Medium, or Large
- Allows tipping which increases price by 1

## How to Run

pipenv install
pipenv shell
pytest -x

## Testing

Separate test files exist for:
- Book class
- Coffee class

Run individually:

pytest -x testing/book_test.py
pytest -x testing/coffee_test.py

## Author

Patrick Mutua