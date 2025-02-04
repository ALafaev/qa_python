import pytest

from main import BooksCollector

class TestBooksCollector:

    valid_books_names = ['А','Гордость и предубеждение и зомби','Что делать, если ваш кот хочет вас убить']
    invalid_books_names = ['','Что делать, если ваш кот хочет вас убить!']
    valid_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    @pytest.mark.parametrize('book', valid_books_names)
    def test_add_new_book_name_length_is_1_32_40_symbols_book_added(self, bookscollector, book):
        bookscollector.add_new_book(book)

        assert len(bookscollector.get_books_genre()) == 1

    @pytest.mark.parametrize('book', invalid_books_names)
    def test_add_new_book_name_is_empty_string_or_more_then_40_symbols_dont_added(self, bookscollector, book):
        bookscollector.add_new_book(book)

        assert len(bookscollector.get_books_genre()) == 0

    def test_add_new_book_dont_add_the_same_book_again(self, bookscollector):
        bookscollector.add_new_book('Гордость и предубеждение и зомби')
        bookscollector.add_new_book('Гордость и предубеждение и зомби')

        assert len(bookscollector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', valid_genre)
    def test_set_book_genre_correct_book_and_genre_successfully_added(self, bookscollector, genre):
        bookscollector.add_new_book('Три мушкетера')
        bookscollector.set_book_genre('Три мушкетера', genre)

        assert bookscollector.books_genre['Три мушкетера'] == genre

    def test_set_book_genre_incorrect_genre_dont_added(self, bookscollector):
        bookscollector.add_new_book('Гордость')
        bookscollector.set_book_genre('Гордость', 'Ужас')

        assert not bookscollector.books_genre['Гордость']

    def test_set_book_genre_incorrect_book_name_dont_added(self, bookscollector):
        bookscollector.add_new_book('Гордость')
        bookscollector.set_book_genre('Гордось', 'Ужасы')

        assert len(bookscollector.get_books_genre()) == 1

    def test_get_book_genre_correct_book_name_return_genre(self, bookscollector):
        bookscollector.add_new_book('Гордость')
        bookscollector.set_book_genre('Гордость', 'Ужасы')

        assert bookscollector.get_book_genre('Гордость') == 'Ужасы'

    def test_get_books_with_specific_genre_correct_genre_return_books(self, bookscollector):
        bookscollector.add_new_book('Гордость и предубеждение и зомби')
        bookscollector.add_new_book('Что делать, если ваш кот хочет вас убить')
        bookscollector.add_new_book('Ночной дозор')
        bookscollector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        bookscollector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        bookscollector.set_book_genre('Ночной дозор', 'Ужасы')

        assert bookscollector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Ночной дозор']

    def test_get_books_for_children_return_books_with_correct_age_rating(self, bookscollector):
        bookscollector.add_new_book('Гордость и предубеждение и зомби')
        bookscollector.add_new_book('Что делать, если ваш кот хочет вас убить')
        bookscollector.add_new_book('Ночной дозор')
        bookscollector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        bookscollector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        bookscollector.set_book_genre('Ночной дозор', 'Ужасы')

        assert bookscollector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_a_new_book_from_books_genre_successfully_appended(self, bookscollector):
        bookscollector.add_new_book('Гордость и предубеждение и зомби')
        bookscollector.add_new_book('Ночной дозор')
        bookscollector.add_book_in_favorites('Ночной дозор')

        assert bookscollector.get_list_of_favorites_books() == ['Ночной дозор']

    def test_delete_book_from_favorites_successfully_deleted(self, bookscollector):
        bookscollector.add_new_book('Ночной дозор')
        bookscollector.add_book_in_favorites('Ночной дозор')
        bookscollector.delete_book_from_favorites('Ночной дозор')

        assert bookscollector.get_list_of_favorites_books() == []






