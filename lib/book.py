#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

if __name__ == "__main__":
    print("=== Creating a book ===")
    book = Book(input("Enter the book title: "), int(input("Enter the page count: ")))

    print(f"\nBook Title: {book.title}")
    print(f"Page Count: {book.page_count}") 

    book.turn_page()

    print("\n--- Testing book property validation ---")
    book.page_count = 200
    print(f"Updated page count: {book.page_count}")   

    book.page_count = "250"
    print(f"Page Count after invalid input: {book.page_count}")                 
    
        