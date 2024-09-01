import pytest
from library_management_system import Library, Book

def test_add_book():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    assert '123-4-5-6-0' in library.books

def test_borrow_book():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    library.borrow_book('123-4-5-6-0')
    assert not library.books['123-4-5-6-0'].available

def test_return_book():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    library.borrow_book('123-4-5-6-0')
    library.return_book('123-4-5-6-0')
    assert library.books['123-4-5-6-0'].available

def test_view_available_books():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    available_books = library.view_available_books()
    assert 'Habits' in available_books
