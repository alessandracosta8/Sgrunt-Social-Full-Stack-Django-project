"""
Imports:
"""
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """ Form to submit post """
    # removed label above form
    # setup attributes for the text area
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Share your thoughts...'
            })
    )

    # image upload
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']


class CommentForm(forms.ModelForm):
    """ Form to submit comment """
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Comment here...'
            })
    )

    class Meta:
        model = Comment
        fields = ['comment']
