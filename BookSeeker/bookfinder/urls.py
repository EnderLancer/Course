from django.urls import path

from .views import BooksListView, BooksSearchResultsView, BookPageView

urlpatterns = [
    path('', BooksListView.as_view(), name='books'),
    path('search/', BooksSearchResultsView.as_view(), name='books_search'),
    path('<int:pk>/', BookPageView.as_view(), name='book'),
]