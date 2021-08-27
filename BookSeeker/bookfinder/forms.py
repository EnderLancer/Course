from django import forms

from bookfinder.models import ReviewComment


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=255)

    class Meta:
        model = ReviewComment
        fields = ['text', ]
