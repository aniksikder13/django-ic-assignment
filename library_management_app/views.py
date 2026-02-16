from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .models import Book, Author, Category

# Create your views here.
class BookList(ListView):
    model = Book
    ordering = ('-created_at',)
    context_object_name = 'books'

    paginate_by = 10
    template_name = "library/books.html"


class BookDetail(DetailView):
    model = Book
    template_name = "library/book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    http_method_names = ("post",)