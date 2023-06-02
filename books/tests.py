from django.test import RequestFactory, TestCase
from django.urls import reverse
from .models import Author, Book
from .views import books_list, book_detail

class BooksListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('main')
        self.author = Author.objects.create(name='Author 1', bio='Bio 1')
        self.book1 = Book.objects.create(title='Book 1', description='Description 1',
                                         publication_date='2023-01-01', cover_image='book1.jpg',
                                         price='9.99')
        self.book1.authors.add(self.author)
        self.book2 = Book.objects.create(title='Book 2', description='Description 2',
                                         publication_date='2023-02-01', cover_image='book2.jpg',
                                         price='14.99')
        self.book2.authors.add(self.author)

    def test_books_list(self):
        request = self.factory.get(self.url)
        response = books_list(request)
        self.assertEqual(response.status_code, 200)

class BookDetailTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = Author.objects.create(name='Author', bio='Bio')
        self.book = Book.objects.create(title='Book', description='Description',
                                        publication_date='2023-01-01', cover_image='book.jpg',
                                        price='9.99')
        self.book.authors.add(self.author)
        self.url = reverse('book_detail', args=[self.book.pk])

    def test_book_detail(self):
        request = self.factory.get(self.url)
        response = book_detail(request, self.book.pk)
        self.assertEqual(response.status_code, 200)