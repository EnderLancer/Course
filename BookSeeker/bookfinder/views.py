from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, CreateView

from bookfinder.forms import CommentForm
from bookfinder.models import Book, BookReview, ReviewComment
from django.contrib.auth.forms import UserCreationForm


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
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        reply_pk = self.request.POST.get('reply_pk')
        if not reply_pk:
            reply_pk = None
        comment = ReviewComment.objects.create(review=context['review'], author=self.request.user, text=form.data['text'], answer_on_id=reply_pk)
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


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')
    success_message = "Your profile was created successfully"

    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        return context
