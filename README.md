# Bookstore Application (Book & Coffee System)

## Overview
This application models a simple bookstore system using Python classes. It demonstrates object-oriented programming concepts such as classes, attributes, methods, encapsulation, and user input handling.

The system allows users to create and interact with:
- A **Book object** (for reading simulation)
- A **Coffee object** (for managing store beverages)

---

## Features

### Book Class
The Book class represents a digital or physical book.

#### Attributes:
- `title` (string): The name of the book (user input)
- `page_count` (integer): Number of pages in the book (validated)

#### Methods:
- `turn_page()`: Simulates reading by printing a message:

### Flipping the page...wow, you read fast!

#### Validation Rules:
- `page_count` must be an integer
- If not valid, an error message is displayed:

### page_count must be an integer

---

### Coffee Class
The Coffee class represents drinks sold in the bookstore café.

#### Attributes:
- `size` (string): Must be `Small`, `Medium`, or `Large`
- `price` (float): Price of the coffee

#### Methods:
- `tip()`: Increases coffee price by 1 and prints a message:

### size must be Small, Medium, or Large


---

## User Interaction Flow

When the program runs, the user is prompted to:

1. Enter book details:
   - Title
   - Page count

2. Enter coffee details:
   - Size
   - Price

3. The system then:
   - Creates a Book object
   - Creates a Coffee object
   - Displays book details
   - Simulates page turning
   - Displays coffee details
   - Applies tip and updates price

---

## Example Output
Enter book title: Python Basics
Enter page count: 200

Enter coffee size (Small, Medium, Large): Medium
Enter coffee price: 4.50

Book: Python Basics
Pages: 200
Flipping the page...wow, you read fast!

Coffee Size: Medium
Price: $4.50
This coffee is great, here's a tip!
New Price: $5.50


---

## Project Structure

project/
│
├── book.py # Book class definition
├── coffee.py # Coffee class definition
└── main.py # Runs the application (user interaction)


---

## Concepts Used
- Object-Oriented Programming (OOP)
- Classes and Objects
- Encapsulation
- Input validation
- Conditional logic
- User input handling

---

## How to Run the Application

1. Ensure Python is installed:

python --version

### Run the program:

- python main.py

### Display Image

Screenshot 2026-06-10 013112.png

### Author

Python OOP Practice Project – Bookstore System

