from library_management_system.library_management_system import Library


def test_return_book():
    library = Library()
    library.add_book('123-4-5-6-0', 'Habits', 'Robert', 2015)
    library.borrow_book('123-4-5-6-0')
    library.return_book('123-4-5-6-0')
    assert library.books['123-4-5-6-0'].available
