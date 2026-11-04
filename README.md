## Bookstore OOP Lab

### Description
This project demonstrates object-oriented programming in Python using two classes: `Book` and `Coffee`.

### Features
- **Book:** Stores a title and page count.
- **Page Count Validation:** Ensures page counts are integers.
- **Turn Page:** Displays a message when a page is turned.
- **Coffee:** Stores a size and price.
- **Size Validation:** Accepts only Small, Medium, or Large.
- **Tip:** Increases the coffee's price by $1.

### Setup
1. Clone the repository.
2. Install Python 3.10.
3. Install dependencies:

   ```bash
   pipenv install
   ```

### Running Tests
Run:

```bash
pipenv run pytest -x
```

### Project Files
- `lib/book.py` — Contains the Book class.
- `lib/coffee.py` — Contains the Coffee class.