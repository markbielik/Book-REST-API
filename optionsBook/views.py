from rest_framework import generics

from .models import Books
from .serializers import BookSerializer


class ListBooksView(generics.ListCreateAPIView):
    """
    View create list all books form database
    and we have options to add new book to database.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def get_view_name(self):
        return "Books List"


class DetailBookView(generics.RetrieveUpdateDestroyAPIView):
    """
    Print detail single book.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def get_view_name(self):
        return "Book Detail"
