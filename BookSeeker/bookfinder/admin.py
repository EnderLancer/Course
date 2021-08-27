from django.contrib import admin

from bookfinder.models import Book, Genre, Author, BookReview, ReviewComment

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(BookReview)
admin.site.register(ReviewComment)
