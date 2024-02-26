# Тесты для тестирования класса BooksCollector

## Описание тестов

- **test_add_new_book_add_two_books** - позитивный тест. Добавление двух книг
- **test_add_new_book_invalid_name** - негативный тест. Добавление книги с недопустимым названием
- **test_set_book_genre_for_one_book** - позитивный тест. Устанавливаем книге жанр
- **test_get_book_genre_for_one_book** - позитивный тест. Получаем жанр книги по её имени
- **test_get_books_with_specific_genre_for_two_books** - позитивный тест. Выводим список книг с определённым жанром
- **test_get_books_genre_two_books_for_two_books** - позитивный тест. Получаем словарь books_genre
- **test_get_books_for_children_positive_for_two_books** - позитивный тест. Возвращаем книги, подходящие детям
- **test_add_book_in_favorites_for_one_book** - позитивный тест. Добавляем книгу в Избранное
- **test_add_book_in_favorites_missing_in_books_genre** - негативный тест. Добавить книгу в избранное, которой нет в списке книг
- **test_delete_book_from_favorites_for_one_book** - позитивный тест. Удаляем книгу из Избранного
- **test_get_list_of_favorites_books_for_two_books** - Позитивный тест. Получаем список Избранных книг
- **README.md** - содержит информацию о проекте

## Запуск тестов
```sh
pytest -v tests.py 
```

