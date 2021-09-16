from django.urls import reverse
from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField

from bookfinder.models import Book, Author, Genre


class BookListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'url', 'name', 'genres', 'authors', 'writing_date']


class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'genres', 'authors', 'description', 'writing_date', 'picture_src']


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'url', 'full_name', 'biography']


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
