from django.contrib import admin
from .models import Author, Book, Category


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at')
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_per_page = 10


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'status')
    list_editable = ('status', )
    list_filter = ('status', 'published_date', 'author', 'category')
    list_per_page = 10


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)