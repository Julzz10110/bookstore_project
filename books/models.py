import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from categories.models import Category



class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category = models.ForeignKey(Category,
                                 related_name='books',
                                 on_delete=models.CASCADE,
                                 verbose_name="Жанр")

    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name="Обложка")
    description = models.TextField(blank=True, verbose_name="Описание")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    class Meta:
        ordering = ('title',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        permissions = [
            ('special_status', '???'),
        ]
