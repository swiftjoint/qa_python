import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name, expected_count', [
        ('Книга ровно сорок символов12345678901234', 1),
        ('', 0)
    ])
    def test_add_new_book_add_two_books(self, name, expected_count):
        book = BooksCollector()
        book.add_new_book(name)

        assert len(book.books_genre) == expected_count

    def test_add_new_book_without_genre(self):
        book = BooksCollector()
        book.add_new_book('Человек паук и робен')

        assert book.get_books_genre() == {'Человек паук и робен': ''}

    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Страх и ненависть в Лас Вегасе', 'Ужасы'),
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

    def test_add_book_in_favorites_adds_book_to_favorites(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(book.favorites) == 1

    def test_delete_book_from_favorites_remove_books(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(book.favorites) == 0

    def test_get_list_of_favorites_books_get_list_favorites(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert book.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
