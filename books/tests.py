from unittest import TestCase
from .models import Book
from categories.models import Category
from accounts.models import CustomUser
from datetime import datetime

class BookTestCase(TestCase):
  def setUp(self):
    self.test_book = Book.objects.create(
    category = Category.objects.first(),
    title = 'Test book title',
    author = 'Test book author',
    price = 100,
    description = 'An interesting book.',
    available = True,
    created = datetime.now(),
    seller = CustomUser.objects.first()
    )

  def test_book_created(self):
    self.assertEqual(self.test_book.category, Category.objects.first())
    self.assertEqual(self.test_book.title, 'Test book title')
    self.assertEqual(self.test_book.author, 'Test book author')
    self.assertEqual(self.test_book.price, 100)
    self.assertEqual(self.test_book.description, 'An interesting book.')
    self.assertEqual(self.test_book.available, True)