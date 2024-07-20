import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_check_added_book_in_collection(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.books_genre

    def test_add_new_book_check_genre_is_None(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == None

    def test_set_book_genre_set_genre_to_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби' , 'Фантастика')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Фантастика'

    @pytest.mark.parametrize ('book_name, expected_genre',[('Акула', 'Ужасы'),('Властелин колец', 'Фантастика')])
    def test_get_book_genre_get_two_genres(self, book_name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('Акула')
        collector.set_book_genre('Акула' , 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец' , 'Фантастика')

        assert collector.get_book_genre(book_name) == expected_genre

    def test_get_books_with_specific_genre_get_list_books_fantasy(self):
        collector = BooksCollector()
        collector.add_new_book('Акула')
        collector.set_book_genre('Акула' , 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец' , 'Фантастика')
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')

        assert result == ['Властелин колец', 'Ведьмак']

    def test_get_books_genre_get_all_list_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Акула')
        collector.set_book_genre('Акула' , 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец' , 'Фантастика')
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.add_new_book('Головоломка')
        collector.set_book_genre('Головоломка', 'Мультфильмы')
        collector.add_new_book('Прянности и страсти')
        collector.set_book_genre('Прянности и страсти', 'Комедии')
        result = {'Акула': 'Ужасы', 'Властелин колец': 'Фантастика', 'Ведьмак': 'Фантастика', 'Головоломка': 'Мультфильмы', 'Прянности и страсти': 'Комедии'}

        assert result == collector.get_books_genre()

    def test_get_books_for_children_select_book_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Акула')
        collector.set_book_genre('Акула' , 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец' , 'Фантастика')
        collector.add_new_book('Убить Билла')
        collector.set_book_genre('Убить Билла', 'Детектив')
        collector.add_new_book('Головоломка')
        collector.set_book_genre('Головоломка', 'Мультфильмы')
        collector.add_new_book('Прянности и страсти')
        collector.set_book_genre('Прянности и страсти', 'Комедии')
        result = ['Властелин колец', 'Головоломка', 'Прянности и страсти']

        assert result == collector.get_books_for_children()

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Головоломка')
        collector.set_book_genre('Головоломка', 'Мультфильмы')
        collector.add_new_book('Прянности и страсти')
        collector.set_book_genre('Прянности и страсти', 'Комедии')
        collector.add_book_in_favorites('Головоломка')
        result = ['Головоломка']

        assert result == collector.favorites


    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Головоломка')
        collector.set_book_genre('Головоломка', 'Мультфильмы')
        collector.add_new_book('Прянности и страсти')
        collector.set_book_genre('Прянности и страсти', 'Комедии')
        collector.add_book_in_favorites('Головоломка')
        collector.add_book_in_favorites('Прянности и страсти')
        collector.delete_book_from_favorites('Головоломка')
        result = ['Прянности и страсти']

        assert result == collector.favorites

    def test_get_list_of_favorites_books_get_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Головоломка')
        collector.set_book_genre('Головоломка', 'Мультфильмы')
        collector.add_new_book('Прянности и страсти')
        collector.set_book_genre('Прянности и страсти', 'Комедии')
        collector.add_book_in_favorites('Головоломка')
        collector.add_book_in_favorites('Прянности и страсти')

        result = ['Головоломка', 'Прянности и страсти']

        assert result == collector.get_list_of_favorites_books()






