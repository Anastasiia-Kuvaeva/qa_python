import pytest

from main import BooksCollector


class TestBooksCollector:

    # Позитивный тест. Добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # Негативный тест. Добавление книги с недопустимым названием
    @pytest.mark.parametrize('name', ['Гарри Поттер и затерянная книга заколдованного города', ''])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # Позитивный тест. Устанавливаем книге жанр
    def test_set_book_genre_for_one_book(self):
        name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector = BooksCollector()
        self.add_book_with_genre_to_books_genre(collector, name, genre)
        assert collector.books_genre[name] == genre

    # Позитивный тест. Получаем жанр книги по её имени
    def test_get_book_genre_for_one_book(self):
        name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector = BooksCollector()
        self.add_book_with_genre_to_books_genre(collector, name, genre)
        assert collector.get_book_genre(name) == genre

    # Позитивный тест. Выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_for_two_books(self):
        etalon_genre = 'Фантастика'
        books = {'Гордость и предубеждение и зомби': etalon_genre,
                 'Гарри Поттер и филосовский камень': etalon_genre}
        collector = BooksCollector()
        # добавление книг в books_genre
        for name, genre in books.items():
            self.add_book_with_genre_to_books_genre(collector, name, genre)
        # проверка, что с данным жанром у нас 2 книги
        assert len(collector.get_books_with_specific_genre(etalon_genre)) == 2

    # Позитивный тест. Получаем словарь books_genre
    def test_get_books_genre_two_books_for_two_books(self):
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Гарри Поттер и филосовский камень': 'Фантастика'}
        collector = BooksCollector()
        for name, genre in books.items():
            self.add_book_with_genre_to_books_genre(collector, name, genre)
        assert collector.get_books_genre() == books

    # Позитивный тест. Возвращаем книги, подходящие детям
    def test_get_books_for_children_positive_for_two_books(self):
        books_adult = {'Гордость и предубеждение и зомби': 'Ужасы',
                       'Филосовский камень': 'Детективы'}
        books_children = {'Маша и медведь': 'Мультфильмы',
                          'Один дома': 'Комедии'}
        books_children_names = []
        collector = BooksCollector()
        for name, genre in books_adult.items():
            # добавление книги в books_genre
            self.add_book_with_genre_to_books_genre(collector, name, genre)
        for name, genre in books_children.items():
            # добавление книги в books_genre
            self.add_book_with_genre_to_books_genre(collector, name, genre)
            books_children_names.append(name)
        assert collector.get_books_for_children() == books_children_names

    # Позитивный тест. Добавляем книгу в Избранное
    def test_add_book_in_favorites_for_one_book(self):
        name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector = BooksCollector()
        # добавление книги в books_genre
        self.add_book_with_genre_to_books_genre(collector, name, genre)
        # добавление книги в избранные
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 1
        assert collector.favorites[0] == name

    # Негативный тест. Добавить книгу в избранное, которой нет в списке книг
    def test_add_book_in_favorites_missing_in_books_genre(self):
        name = 'Гарри Поттер'
        collector = BooksCollector()
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 0

    # Позитивный тест. Удаляем книгу из Избранного
    def test_delete_book_from_favorites_for_one_book(self):
        name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector = BooksCollector()
        # добавление книги в books_genre
        self.add_book_with_genre_to_books_genre(collector, name, genre)
        # добавление книги в избранные
        collector.add_book_in_favorites(name)
        # удаление книги из избранных
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == 0

    # Позитивный тест. Получаем список Избранных книг
    def test_get_list_of_favorites_books_for_two_books(self):
        books = {'Гордость и предубеждение и зомби': 'Ужасы',
                 'Гарри Поттер': 'Фантастика'}
        favorites_books_names = []
        collector = BooksCollector()
        for name, genre in books.items():
            # добавление книги в books_genre
            self.add_book_with_genre_to_books_genre(collector, name, genre)
            # добавление книги в избранные
            collector.add_book_in_favorites(name)
            favorites_books_names.append(name)
        assert collector.get_list_of_favorites_books() == favorites_books_names

    # Вспомогательный метод. Добавление книги с жанром в словарь books_genre
    def add_book_with_genre_to_books_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
