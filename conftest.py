import pytest

from main import BooksCollector

@pytest.fixture # фикстура, которая создаёт экземпляр класса BooksCollector
def bookscollector():
    bookscollector = BooksCollector()

    return bookscollector