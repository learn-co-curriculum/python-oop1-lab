# testing/coffee_test.py
# Test suite for the Coffee class.

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from coffee import Coffee


class TestCoffee:
    """Tests for the Coffee class."""

    # ── __init__ ──────────────────────────────────────────────────────────────

    def test_coffee_has_size(self):
        """Coffee stores the size passed in."""
        coffee = Coffee("Medium", 4.50)
        assert coffee.size == "Medium"

    def test_coffee_has_price(self):
        """Coffee stores the price passed in."""
        coffee = Coffee("Medium", 4.50)
        assert coffee.price == 4.50

    # ── size property ─────────────────────────────────────────────────────────

    def test_size_small_is_valid(self):
        """Small is a valid size."""
        coffee = Coffee("Small", 3.00)
        assert coffee.size == "Small"

    def test_size_medium_is_valid(self):
        """Medium is a valid size."""
        coffee = Coffee("Medium", 4.00)
        assert coffee.size == "Medium"

    def test_size_large_is_valid(self):
        """Large is a valid size."""
        coffee = Coffee("Large", 5.00)
        assert coffee.size == "Large"

    def test_invalid_size_prints_error(self, capsys):
        """Invalid size prints an error message."""
        coffee = Coffee("Jumbo", 6.00)
        captured = capsys.readouterr()
        assert "size must be Small, Medium, or Large" in captured.out

    def test_invalid_size_sets_none(self):
        """Invalid size results in None being stored."""
        coffee = Coffee("Jumbo", 6.00)
        assert coffee.size is None

    def test_size_can_be_updated(self):
        """Size can be updated to another valid size."""
        coffee = Coffee("Small", 3.00)
        coffee.size = "Large"
        assert coffee.size == "Large"

    def test_size_update_invalid(self, capsys):
        """Updating size with an invalid value prints an error."""
        coffee = Coffee("Small", 3.00)
        coffee.size = "Venti"
        captured = capsys.readouterr()
        assert "size must be Small, Medium, or Large" in captured.out

    # ── tip() ─────────────────────────────────────────────────────────────────

    def test_tip_prints_message(self, capsys):
        """tip() prints the correct message."""
        coffee = Coffee("Medium", 4.50)
        coffee.tip()
        captured = capsys.readouterr()
        assert "This coffee is great, here's a tip!" in captured.out

    def test_tip_increases_price_by_one(self):
        """tip() increases the price by 1."""
        coffee = Coffee("Medium", 4.50)
        coffee.tip()
        assert coffee.price == 5.50

    def test_tip_can_be_called_multiple_times(self):
        """Each call to tip() increases price by 1."""
        coffee = Coffee("Large", 5.00)
        coffee.tip()
        coffee.tip()
        assert coffee.price == 7.00