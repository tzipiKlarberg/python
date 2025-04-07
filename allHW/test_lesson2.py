import pytest
import  book
import library



def test_add_book():
    book1 = book.Book("lidor","rachel")
    library1 = library.Library()
    library1.add_book(book1)
    assert library1.books[0] == book1

def test_add_user():
    library1 = library.Library()
    library1.add_user("natan")
    assert library1.users[0] == "natan"

def test_dont_add_not_exist_book():
    library1 = library.Library()
    length = len(library1.checked_out_books)
    library1.add_user("natan")
    try:
        library1.check_out_book("natan",book.Book("lidor", "rachel"))
    except ValueError:
        assert len(library1.checked_out_books) == length

def test_dont_pop_not_exist_book():
    library1 = library.Library()
    length = len(library1.checked_out_books)
    library1.add_user("natan")
    try:
        library1.return_book("natan", book.Book("lidor", "rachel"))
    except ValueError as e:
        assert len(library1.checked_out_books) == length
def test_search_return_empty():
    library1 = library.Library()
    assert library1.search_books("lidor") == []