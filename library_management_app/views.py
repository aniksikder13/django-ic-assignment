from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Book, Author, Category
from .form import BookForm


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


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    # success_url = reverse_lazy("blog_detail")
    template_name = "library/form.html"

    def get_success_url(self):
        return reverse('blog_detail', kwargs={"pk": self.object.pk})

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("books")
    template_name = "library/form.html"