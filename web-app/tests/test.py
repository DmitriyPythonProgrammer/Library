from tests.tests_class.book.test_books import BookTests
from tests.tests_class.author.test_authors import AuthorTests


def test_main():
    author_tests = AuthorTests()

    author_tests.test_create_author()

    author_tests.test_read_author()

    author_tests.test_read_authors()

    book_tests = BookTests(author_tests.test_id)

    book_tests.test_create_book()

    book_tests.test_read_book()

    book_tests.test_read_books()

    book_tests.test_delete_book()

    book_tests.test_read_deleted_book()

    author_tests.test_delete_author()

    author_tests.test_read_deleted_authors()


