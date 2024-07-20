# qa_python
# Тестовый набор для BooksCollector

Hепозиторий содержит набор тестов для класса `BooksCollector`, 
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

1. **test_add_new_book_add_two_books**: Проверяет, что при добавлении двух 
книг коллекция содержит ровно две книги.
2. **test_add_new_book_check_added_book_in_collection**: Проверяет, что 
недавно добавленная книга присутствует в коллекции.
3. **test_add_new_book_check_genre_is_None**: Убеждается, что у недавно 
добавленной книги жанр установлен в `None`.
4. **test_set_book_genre_set_genre_to_book**: Тестирует установку жанра 
для конкретной книги.
5. **test_get_book_genre_get_two_genres**: Использует параметризованный 
тест для проверки получения жанров для разных книг.
6. **test_get_books_with_specific_genre_get_list_books_fantasy**: 
Проверяет список книг, возвращаемых для конкретного жанра.
7. **test_get_books_genre_get_all_list_with_genre**: Проверяет всю 
коллекцию книг с их жанрами.
8. **test_get_books_for_children_select_book_for_children**: Тестирует 
выбор книг, подходящих для детей.
9. **test_add_book_in_favorites_add_two_books**: Проверяет добавление книг 
в список избранного.
10. **test_delete_book_from_favorites_delete_one_book**: Тестирует 
удаление книги из списка избранного.
11. **test_get_list_of_favorites_books_get_favorites**: Проверяет 
получение списка избранных книг.

## Запуск тестов

Для запуска тестов необходимо  установить `pytest`. Запуск тестов 
осуществляется через консоль:

pytest -v tests.py

## Вклад
Всегда можно улучшить и увеличить тесты.

## Лицензия
Yandex_Practicum
