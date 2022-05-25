from django.urls import path

from .views import ListBooksView, DetailBookView, ApiSpecification, SearchAuthorsView, ImportBooks

urlpatterns = [
    path('api_spec/', ApiSpecification.as_view(), name='api_spec'),
    path('books/', ListBooksView.as_view(), name="books_list"),
    path('books/<int:pk>/', DetailBookView.as_view(), name="book_detail"),
    path('search/', SearchAuthorsView.as_view(), name="search_authors"),
    path('import/', ImportBooks.as_view(), name="import_books")
]
