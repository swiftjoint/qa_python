# qa_python

Список тестов

Название теста: test_add_new_book_add_two_books
Проверка: Увеличение количества книг при добавлении двух книг, 1 книга 40 символов; 2 книга ноль символов.
Тестируемый метод: add_new_book

Название теста: test_add_new_book_without_genre
Проверка: Проверка, что книга добавлена без жанра.
Тестируемый метод: add_new_book и get_books_genre

Название теста: test_set_book_genre_existing_book_valid_genre
Проверка: Установка жанра существующей книги и его правильное получение.
Тестируемый метод: set_book_genre и get_book_genre

Название теста: test_get_book_genre_returns_name_book
Проверка: Проверка правильного получения жанра для существующей книги.
Тестируемый метод: set_book_genre и get_book_genre

Название теста: test_get_books_with_specific_genre_returns_list_book
Проверка: Проверка, что книга добавляется в список книг с конкретным жанром.
Тестируемый метод: add_new_book, set_book_genre и get_books_with_specific_genre

Название теста: test_get_books_genre_returns_current_dictionary
Проверка: Проверка, что возвращается правильный словарь книг и их жанров.
Тестируемый метод: add_new_book, set_book_genre и get_books_genre

Название теста: test_get_books_for_children_returns_books_without_age_rating
Проверка: Проверка, что книги без возрастного рейтинга попадают в список для детей.
Тестируемый метод: get_books_for_children

Название теста: test_add_book_in_favorites_adds_book_to_favorites
Проверка: Проверка, что книга добавляется в список избранных.
Тестируемый метод: add_book_in_favorites

Название теста: test_delete_book_from_favorites_remove_books
Проверка: Проверка, что книга удаляется из списка избранных.
Тестируемый метод: delete_book_from_favorites

Название теста: test_get_list_of_favorites_books_get_list_favorites
Проверка: Проверка, что возвращается правильный список избранных книг.
Тестируемый метод: get_list_of_favorites_books