from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'subject', 'publication_date', 'language')

admin.site.register(Book, BookAdmin)
