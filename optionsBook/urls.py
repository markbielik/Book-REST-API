from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ListBooksViewSet, DetailBookView, \
    ApiSpecification, SearchAuthorsView, ImportBooks  # ListBooksView

router = DefaultRouter()
router.register('books', ListBooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api_spec/', ApiSpecification.as_view(), name='api_spec'),
    # path('books/', ListBooksView.as_view(), name="books_list"),
    path('books/<int:pk>/', DetailBookView.as_view(), name="book_detail"),
    path('search/', SearchAuthorsView.as_view(), name="search_authors"),
    path('import/', ImportBooks.as_view(), name="import_books")
]
