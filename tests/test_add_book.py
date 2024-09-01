import pytest
from library_management_system import Library, Book

def test_add_book():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    assert '123-4-5-6-0' in library.books
    assert library.books['123-4-5-6-0'].title == 'Habits'
    assert library.books['123-4-5-6-0'].author == 'Robert'
    assert library.books['123-4-5-6-0'].publication_year == 2015
    assert library.books['123-4-5-6-0'].available == True

