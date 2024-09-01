from library_management_system.library_management_system import Library


def test_view_available_books():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    library.add_book('978-1-23-456789-7', 'Book Two', 'Author B', 2022)
    library.borrow_book('123-4-5-6-0')
    available_books = library.view_available_books()
    
    assert 'Book One' not in available_books  
    assert 'Book Two' in available_books  
