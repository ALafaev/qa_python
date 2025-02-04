# qa_python
1. `test_add_new_book_name_length_is_1_32_40_symbols_book_added` - Проверка метода add_new_book на добавление книги с длиной названия 1, 32, 40 символов.
2. `test_add_new_book_name_is_empty_string_or_more_then_40_symbols_dont_added` - Метод add_new_book не добавляет книгу с длиной названия более 40 символов или без названия (пустая строка).
3. `test_add_new_book_dont_add_the_same_book_again` - Метод add_new_book не добавит в словарь books_genre книгу, которая там уже есть.
4. ` test_set_book_genre_correct_book_and_genre_successfully_added` - Метод set_book_genre позволяет присвоить жанр книге, которая есть в списке books_genre
5. `test_set_book_genre_incorrect_genre_dont_added` - Метод set_book_genre не присвоит книге жанр, если названия жанра нет в списке self.genre
6. `test_set_book_genre_incorrect_book_name_dont_added` - Метод set_book_genre не присвоит книге жанр, если названия книги нет в списке books_genre
7. ` test_get_book_genre_correct_book_name_return_genre` - Метод get_book_genre возвращает жанр книги по ее названию
8. ` test_get_books_with_specific_genre_correct_genre_return_books` - Проверка что метод get_books_with_specific_genre возвращает список книг определенного жанра
9. ` test_get_books_for_children_return_books_with_correct_age_rating` - Проверка что метод get_books_for_children возвращает из всего словаря books_genre только книги, подходящие по возрастному рейтингу для детей.
10. `test_add_book_in_favorites_a_new_book_from_books_genre_successfully_appended` - Проверка, что метод add_book_in_favorites добавляет книгу в список избранного  self.favorites по ее названию
11. ` test_delete_book_from_favorites_successfully_deleted` - Проверка, что метод delete_book_from_favorites удаляет книгу из списка self.favorites по ее названию