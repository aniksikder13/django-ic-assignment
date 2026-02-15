from django.contrib import admin
from .models import Author, Book, Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'status')
    list_editable = ('status', )
    list_filter = ('status', 'published_date', 'author', 'category')
    list_per_page = 10


admin.site.register(Book, BookAdmin)