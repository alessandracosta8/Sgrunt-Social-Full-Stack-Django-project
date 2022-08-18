"""
Imports:
"""
from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm


class PostListView(View):
    """
    Handles http request that come to this url
    """
    def get(self, request, *args, **kwargs):
        """ Iterate through posts and display them from newest to last """
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'core/post_list.html', context)

    def post(self, request, *args, **kwargs):
        """ Handles post request and saves the new post """
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
        
        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'core/post_list.html', context)
