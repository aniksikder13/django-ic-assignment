from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('add-book/', BookList.as_view(), name='add-book'),
    path('<uuid:pk>/', BookDetail.as_view(), name='blog_detail'),
]
