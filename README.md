# qa_python
# Тестовый набор для BooksCollector

Репозиторий содержит набор тестов для класса `BooksCollector`, 
написанных с использованием фреймворка `pytest`. Тесты проверяют  
правильность работы методов класса `BooksCollector`.

## Обзор

Класс `BooksCollector` позволяет установить жанр книг и добавить их в 
избранное.

## Структура

- **main.py**: Содержит реализацию класса `BooksCollector`.
- **test_books_collector.py**: Содержит тестовые случаи для класса 
`BooksCollector`.

## Тесты

Тестовые случаи организованы в классе `TestBooksCollector`. Описание 
тестов:

## Фикстура collector:

Используется для создания экземпляра класса BooksCollector перед каждым 
тестом.
Фикстура определена в файле conftest.py.

## Запуск тестов
1. test_add_new_book_add_two_books:
Проверяет добавление двух книг.
Убеждается, что в коллекции действительно две книги, проверяя длину 
словаря books_genre.
2. test_add_new_book_check_added_book_in_collection:
Проверяет, что добавленная книга присутствует в коллекции.
3. test_add_new_book_check_genre_is_empty:
Проверяет, что жанр добавленной книги по умолчанию пустой (например, 
пустая строка).
4. test_add_new_book_check_valid_length_of_name:
Проверяет, что книга с невалидным именем (например, пустая строка или 
слишком длинное имя) не добавляется в коллекцию.
5. test_set_book_genre_set_genre_to_book:
Проверяет установку жанра для книги.
6. test_set_book_genre_set_invalid_genre:
Проверяет, что установка невалидного жанра приводит к ожидаемому 
результату (например, пустой строке).
7. test_get_book_genre_get_two_genres:
Проверяет получение жанра для двух разных книг с различными жанрами.
8. test_get_books_with_specific_genre_get_list_books_fantasy:
Проверяет получение списка книг определенного жанра (например, 
"Фантастика").
9. test_get_books_genre_get_all_list_with_genre:
Проверяет получение полного списка книг с их жанрами.
10. test_get_books_for_children_select_book_for_children:
Проверяет отбор книг для детей.
11. test_add_book_in_favorites_add_two_books:
Проверяет добавление книг в список избранных.
12. test_delete_book_from_favorites_delete_one_book:
Проверяет удаление книги из списка избранных.
13. test_get_list_of_favorites_books_get_favorites:
Проверяет получение списка избранных книг.
Для запуска тестов необходимо  установить `pytest`. Запуск тестов 
осуществляется через консоль:

pytest -v tests.py

## Вклад
Всегда можно улучшить и увеличить тесты.

## Лицензия
Yandex_Practicum
