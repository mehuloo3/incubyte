# Library Management System

This is a simple Library Management System implemented in Python, following Test-Driven Development (TDD) principles. The system allows users to:
- Add new books to the library
- Borrow books
- Return books
- View available books

overview:
Library Management System

Project Overview
This project is a simple Library Management System implemented in Python. It allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. The project follows the principles of Test-Driven Development (TDD) and is fully version-controlled using Git.

Features
1.Add Books: Users can add new books to the library, each with a unique identifier (ISBN), title, author, and publication year.
2.Borrow Books: Users can borrow books if they are available. The system checks the availability before allowing a book to be borrowed.
3.Return Books: Users can return borrowed books, and the system updates the book's availability status.
4.View Available Books: Users can view a list of all available books in the library.

Project Structure
The project is organized as follows:

library_management_system/
library_management_system.py # Main implementation file 
tests/ test_add_book.py # Tests for adding books 
│ test_borrow_book.py # Tests for borrowing books │ 
 test_return_book.py # Tests for returning books │ 
 test_view_books.py # Tests for viewing available books ├

Prerequisites

Python 3.11 or higher installed on your machine.
Git installed for version control.
pytest for running the tests.

Set Up the Virtual Environment:
(Optional) It’s recommended to use a virtual environment to manage dependencies:
python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

Install Dependencies:
If you have a requirements.txt file, you can install the required dependencies:
pip install -r requirements.txt

Run the Tests:
Ensure everything is working by running the test suite:

pytest
This will run all the tests located in the tests/ directory.

Development Process
Step 1: Test-Driven Development (TDD)

This project follows the TDD approach:
Write Tests: Before implementing any feature, write a test for it.
Run the Test: Run the test and watch it fail (since the feature isn't implemented yet).
Implement the Feature: Write the code to make the test pass.
Refactor: Clean up your code while ensuring all tests still pass.
Repeat: Continue this process for each feature.
Example

For adding a book:
Write a Test:
In tests/test_add_book.py:
def test_add_book(): library = Library() library.add_book('978-3-16-148410-0', 'Book One', 'Author A', 2021) assert '978-3-16-148410-0' in library.books

Run the Test:
pytest tests/test_add_book.py

