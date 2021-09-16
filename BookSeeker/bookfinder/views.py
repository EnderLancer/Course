from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from bookfinder.forms import CommentForm, ReviewForm
from bookfinder.models import Book, BookReview, ReviewComment, Genre, Author
from bookfinder.serializers import BookListSerializer, BookDetailSerializer, AuthorSerializer, GenreSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'authors', 'genres', 'writing_date']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookDetailSerializer
        return super(BookViewSet, self).retrieve(request, *args, **kwargs)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['full_name']


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class BookPageView(FormMixin, DetailView):
    model = Book
    template_name = 'detail_book.html'
    form_class = CommentForm
    context_object_name = 'book'

    def get_success_url(self):
        return reverse('book', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BookPageView, self).get_context_data(**kwargs)
        context['review'] = BookReview.objects.filter(book=context['book'])
        if context['review']:
            context['review'] = context['review'].first()
            context['comments'] = context['review'].comments.all()
        elif self.request.user.has_perm("bookfinder.add_bookreview"):
            context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (reverse_lazy('login'), request.path))
        self.object = self.get_object()
        context = self.get_context_data()
        if context['review']:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            review_text = self.request.POST.get('text')
            BookReview.objects.create(book=self.object, author=self.request.user, text=review_text)
            return redirect(reverse_lazy('home'))

    def form_valid(self, form):
        context = self.get_context_data()
        reply_pk = self.request.POST.get('reply_pk')
        if not reply_pk:
            reply_pk = None
        comment = ReviewComment.objects.create(review=context['review'], author=self.request.user,
                                               text=form.data['text'], answer_on_id=reply_pk)
        comment.save()
        return super(BookPageView, self).form_valid(form)


class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'books.html'
    context_object_name = 'books'


class BooksSearchResultsView(BooksListView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(name__icontains=query) | Q(authors__full_name__icontains=query),
        ).distinct()
