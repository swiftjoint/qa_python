import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):

        book = BooksCollector()

        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(book.get_books_genre()) == 2

    def test_add_new_book_without_genre(self):
        book = BooksCollector()

        book.add_new_book('Гордость и предубеждение и зомби')

        assert book.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
    ])
    def test_set_book_genre_existing_book_valid_genre(self, name, genre):

        book = BooksCollector()

        book.add_new_book(name)
        book.set_book_genre(name, genre)

        assert book.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ])
    def test_get_book_genre_returns_name_book(self, name, genre):

        book = BooksCollector()

        book.add_new_book(name)
        book.set_book_genre(name, genre)

        assert book.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    ])
    def test_get_books_with_specific_genre_returns_list_book(self, name, genre):

        book = BooksCollector()

        book.add_new_book(name)
        book.set_book_genre(name, genre)

        assert name in book.get_books_with_specific_genre(genre)

    def test_get_books_genre_returns_current_dictionary(self):
        book = BooksCollector()

        book.add_new_book('Гордость и предубеждение и зомби')
        book.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        book.add_new_book('Что делать, если ваш кот хочет вас убить')
        book.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        expected_dict = {
            'Гордость и предубеждение и зомби': 'Фантастика',
            'Что делать, если ваш кот хочет вас убить': 'Ужасы'
        }

        assert book.get_books_genre() == expected_dict

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    ])
    def test_get_books_for_children_returns_books_without_age_rating(self, name, genre):

        book = BooksCollector()

        book.add_new_book(name)
        book.set_book_genre(name, genre)

        books_for_children = book.get_books_for_children()

        if genre not in book.genre_age_rating:
            assert name in books_for_children
        else:
            assert name not in books_for_children

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение и зомби'
    ])
    def test_add_book_in_favorites_adds_book_to_favorites(self, name):

        book = BooksCollector()

        book.add_new_book(name)

        book.add_book_in_favorites(name)

        assert len(book.favorites) == 1

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение и зомби'
    ])
    def test_delete_book_from_favorites_remove_books(self, name):

        book = BooksCollector()

        book.add_new_book(name)
        book.add_book_in_favorites(name)
        book.delete_book_from_favorites(name)

        assert len(book.favorites) == 0

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение и зомби'
    ])
    def test_get_list_of_favorites_books_get_list_favorites(self, name):

        book = BooksCollector()

        book.add_new_book(name)
        book.add_book_in_favorites(name)

        assert book.get_list_of_favorites_books() == [name]
