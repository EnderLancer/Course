from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    biography = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True)
    publication_date = models.DateField(default=timezone.now)
    writing_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')
    picture_src = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name


class BookReview(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='review')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1023)
    publication_date = models.DateField()

    def __str__(self):
        return f'Review on {self.book.name} by {self.author.username}'


class ReviewComment(models.Model):
    review = models.ForeignKey(BookReview, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    publication_date = models.DateTimeField(default=timezone.now)
    answer_on = models.ForeignKey("ReviewComment", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Comment on review {self.review.book.name} by {self.author.username}'
