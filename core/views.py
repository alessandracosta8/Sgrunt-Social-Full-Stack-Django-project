"""
Imports:
- base render
- 
"""
from django.shortcuts import render
from django.views import View
from .models import Post


class PostListView(View):
    """
    Handles http request that come to this url
    """
    def get(self, request, *args, **kwargs):
        """ Iterate through posts and display them from newest to last """
        posts = Post.objects.all().order_by('-created_on')

        context = {
            'post_list': posts,
        }

        return render(request, 'core/post_list.html', context)
