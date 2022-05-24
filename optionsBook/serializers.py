from rest_framework import serializers

from .models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id',
                  'external_id',
                  'title',
                  'authors',
                  'publication_year',
                  'acquired_state',
                  'thumbnail')  # other options fields = '__all__'
