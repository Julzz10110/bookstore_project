from django.contrib import admin
from .models import Book
from reviews.models import Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'price',
        'available',
        'created',
    ]

    list_filter = [
        'available',
        'created',
    ]

    list_editable = ['price', 'available']
    inlines = [
        ReviewInline,
    ]
