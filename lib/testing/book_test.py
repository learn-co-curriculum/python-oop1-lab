from lib.book import Book

def test_book_creation():
    book = Book("Harry Potter", 300)
    assert book.title == "Harry Potter"
    assert book.page_count == 300

def test_turn_page(capsys):
    book = Book("Test Book", 100)
    book.turn_page()
    captured = capsys.readouterr()
    assert "Flipping the page" in captured.out