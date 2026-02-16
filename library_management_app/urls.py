from django.urls import path
from .views import BookList, BookDetail, BookDelete

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('library/add-book/', BookList.as_view(), name='add-book'),
    path('library/<uuid:pk>/', BookDetail.as_view(), name='blog_detail'),
    path("library/<uuid:pk>/delete/", BookDelete.as_view(), name="book_delete")
]
