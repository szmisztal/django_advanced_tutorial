from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import new_form
from .models import Author, Book
from .validators import validate_year
from django.core.exceptions import ValidationError
from .forms import NewForm

class LibraryTests(TestCase):

    def test_our_first(self):
        assert 1 == 1

    #urls

    def test_url_new_form(self):
        url = reverse('new_form')
        self.assertEquals(resolve(url).func, new_form)

    def test_view_new_form(self):
        client = Client()
        response = client.get(reverse('new_form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_form.html')

    #models

    def setUp(self):
        self.author = Author.objects.create(name = "Szymon", surname = "Misztal")
        self.book = Book.objects.create(title = "Test", publication_year = 2022, author = self.author)

    def test_author_string(self):
        self.assertEqual(str(self.author), f"{self.author.name} {self.author.surname}")

    def test_book_not_null(self):
        self.assertNotEqual(self.book, None)

    def test_book_is_unique(self):
        with self.assertRaises(Exception):
            Book.objects.create(title = "Test", publication_year = 2022, author = self.author)

    def test_book_manager(self):
        books = Book.books.new_books()
        self.assertGreater(len(books), 0)

    #func

    def test_func_validate_year(self):
        self.assertRaises(ValidationError, validate_year, 2030)

    def test_func_validate_year_2(self):
        self.assertEqual(validate_year(2019), 2019)

    #forms

    def test_new_form_valid(self):
        form = NewForm(data = {
            'name': 'Test',
            'year': 2020
        })
        self.assertTrue(form.is_valid())

    def test_new_form_not_valid(self):
        form = NewForm(data = {
            'name': 'Test',
            'year': 2030
        })
        self.assertFalse(form.is_valid())

    #TDD

    def test_book_method_is_new(self):
        self.assertTrue(self.book.is_new())

    def test_book_method_is_not_new(self):
        book = Book.objects.create(title = 'Test3', publication_year = 1950, author = self.author)
        self.assertFalse(book.is_new())
