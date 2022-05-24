from django.urls import path

from .views import ListBooksView, DetailBookView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books_list"),
    path('books/<int:pk>/', DetailBookView.as_view(), name="book_detail"),
]