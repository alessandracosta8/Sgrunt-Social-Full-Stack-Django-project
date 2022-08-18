"""
Imports:
"""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Inherits from the Post model and only shows the body field
    """
    # removed label above form
    # setup attributes for the text area
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Share your thoughts...'
        })
    )

    class Meta:
        model = Post
        fields = ['body']
