#!/usr/bin/env python3


class Book:
    def __init__(self, title: str, page_count: int) -> None:
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """The page_count property."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self) -> None:
        print("Flipping the page...wow, you read fast!")
