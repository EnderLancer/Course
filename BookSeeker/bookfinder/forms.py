from django import forms

from bookfinder.models import ReviewComment, BookReview


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=255)

    class Meta:
        model = ReviewComment
        fields = ['text', ]


class ReviewForm(forms.ModelForm):
    text = forms.CharField(max_length=1023)

    class Meta:
        model = BookReview
        fields = ['text', ]