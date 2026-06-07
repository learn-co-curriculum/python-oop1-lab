# testing/book_test.py
# Test suite for the Book class.

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from book import Book


class TestBook:
    """Tests for the Book class."""

    # ── __init__ ──────────────────────────────────────────────────────────────

    def test_book_has_title(self):
        """Book stores the title passed in."""
        book = Book("Python Crash Course", 544)
        assert book.title == "Python Crash Course"

    def test_book_has_page_count(self):
        """Book stores the page count passed in."""
        book = Book("Python Crash Course", 544)
        assert book.page_count == 544

    def test_book_title_can_be_changed(self):
        """Book title can be updated after creation."""
        book = Book("Python Crash Course", 544)
        book.title = "Clean Code"
        assert book.title == "Clean Code"

    # ── page_count property ───────────────────────────────────────────────────

    def test_page_count_must_be_integer(self, capsys):
        """Non-integer page_count prints an error message."""
        book = Book("Python Crash Course", "five hundred")
        captured = capsys.readouterr()
        assert "page_count must be an integer" in captured.out

    def test_page_count_invalid_sets_none(self):
        """Non-integer page_count results in None being stored."""
        book = Book("Python Crash Course", "five hundred")
        assert book.page_count is None

    def test_page_count_valid_integer(self):
        """Valid integer page_count is stored correctly."""
        book = Book("Clean Code", 431)
        assert book.page_count == 431

    def test_page_count_can_be_updated(self):
        """page_count can be updated via the setter."""
        book = Book("Clean Code", 431)
        book.page_count = 500
        assert book.page_count == 500

    def test_page_count_update_invalid(self, capsys):
        """Updating page_count with a non-integer prints an error."""
        book = Book("Clean Code", 431)
        book.page_count = "lots"
        captured = capsys.readouterr()
        assert "page_count must be an integer" in captured.out

    # ── turn_page() ───────────────────────────────────────────────────────────

    def test_turn_page_prints_message(self, capsys):
        """turn_page() prints the correct message."""
        book = Book("Python Crash Course", 544)
        book.turn_page()
        captured = capsys.readouterr()
        assert "Flipping the page...wow, you read fast!" in captured.out

    def test_turn_page_can_be_called_multiple_times(self, capsys):
        """turn_page() can be called more than once."""
        book = Book("Python Crash Course", 544)
        book.turn_page()
        book.turn_page()
        captured = capsys.readouterr()
        assert captured.out.count("Flipping the page") == 2