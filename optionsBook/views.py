from json import loads
from urllib.request import urlopen

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Books
from .serializers import BookSerializer


class ListBooksViewSet(viewsets.ModelViewSet):
    """
    View create list all books form database
    and we have options to add new book to database.
    Options filter is active

    You have tried these URL patterns, in this order:
    api_spec/
    books/<int:pk>/
    search/
    import/

    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['authors',
                        'title',
                        'publication_year',
                        'acquired_state']

    def get_view_name(self):
        return "Books List"

# /// This class was left for testing ///
# class ListBooksView(generics.ListCreateAPIView):
#     """
#     View create list all books form database
#     and we have options to add new book to database.
#     Options filter is active
#     """
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['authors',
#                         'title',
#                         'publication_year',
#                         'acquired_state']
#
#     def get_view_name(self):
#         return "Books List"


class DetailBookView(generics.RetrieveUpdateDestroyAPIView):
    """
    Print detail single book.

     You have tried these URL patterns, in this order:
    api_spec/
    books/
    search/
    import/
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def get_view_name(self):
        return "Book Detail"


class ApiSpecification(APIView):
    """
    show a defined api version

     You have tried these URL patterns, in this order:
    books/
    books/<int:pk>/
    search/
    import/
    """
    def get(self, request):
        data = {
            "info": {
                'version': "2022.05.16"
            }
        }
        return Response(data)


class SearchAuthorsView(generics.ListCreateAPIView):
    """
    different version of the search

     You have tried these URL patterns, in this order:
    api_spec/
    books/
    books/<int:pk>/
    import/
    """
    search_fields = ['authors']
    filter_backends = (filters.SearchFilter, )
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class ImportBooks(APIView):
    """
    import books to database from address url

     You have tried these URL patterns, in this order:
    api_spec/
    books/
    books/<int:pk>/
    search/
    """

    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        get_link = request.POST['addressUrl']
        with urlopen(get_link) as response:
            data = loads(response.read())
        items = data.get('items')
        counter = 0
        for i in range(len(items)):
            external_id = items[i].get('id')
            title = items[i].get('volumeInfo').get('title')
            authors = items[i].get('volumeInfo').get('authors')
            published_year = items[i].get('volumeInfo').get('publishedDate')
            published_year = published_year[:4]
            acquired = items[i].get('accessInfo').get('pdf').get('isAvailable')
            thumbnail = items[i].get('volumeInfo').get('previewLink')
            all_book = Books.objects.all()
            if len(all_book.filter(title__contains=title)) > 0 \
                and len(all_book.filter(authors__contains=authors)) > 0:  # duplicate filtering version modification
                if counter == 0:
                    counter = 0
                else:
                    counter -= 1
            else:
                new_book = Books.objects.create(external_id=external_id,
                                                title=title,
                                                authors=authors,
                                                publication_year=published_year,
                                                acquired_state=acquired,
                                                thumbnail=thumbnail)
                new_book.save()
                counter += 1
        data = {
            'imported': counter
        }
        return Response(data)
