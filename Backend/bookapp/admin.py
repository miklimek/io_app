from django.contrib import admin
from .models import Book, Opinion


# Register your models here.
@admin.register(Book)
class BookModel(admin.ModelAdmin):
    list_filter = ('title', 'genres')
    list_display = ('title', 'author')


@admin.register(Opinion)
class OpinionModel(admin.ModelAdmin):
    list_filter = ('book_id', 'user_id')
    list_display = ('book_id', 'user_id')

