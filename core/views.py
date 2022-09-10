"""
Imports:
"""
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm


class PostListView(LoginRequiredMixin, View):
    """
    Post feed view
    """
    def get(self, request, *args, **kwargs):
        """
        Iterate through posts and display them from newest to last
        Filters only the posts from the users that are followed by the user
        """
        logged_in_user = request.user
        posts = Post.objects.filter(
            author__profile__followers__in=[logged_in_user.id]
        ).order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'core/post_list.html', context)

    def post(self, request, *args, **kwargs):
        """ Handles post request and saves the new post """
        logged_in_user = request.user
        posts = Post.objects.filter(
            author__profile__followers__in=[logged_in_user.id]
        ).order_by('-created_on')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'core/post_list.html', context)


class PostDetailView(LoginRequiredMixin, View):
    """ specific post page with its comments """
    def get(self, request, pk, *args, **kwargs):
        """ retrieves post and relative comments """
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'core/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        """ comment added to its post """
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'core/post_detail.html', context)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Ability to edit a post """
    model = Post
    fields = ['body']
    template_name = 'core/post_edit.html'

    def get_success_url(self):
        """ redirect to post detail page when edit is successful """
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        """ If user matches post's author -> can edit, or else -> 403 """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Ability to delete post """
    model = Post
    template_name = 'core/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        """ If user matches post's author -> can delete, or else -> 403 """
        post = self.get_object()
        return self.request.user == post.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Ability to delete comment """
    model = Comment
    template_name = 'core/comment_delete.html'

    def get_success_url(self):
        """ redirect to post detail page when comment delete is successful """
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        """ If user matches comment's author -> can delete, or else -> 403 """
        comment = self.get_object()
        return self.request.user == comment.author


class ProfileView(View):
    """
    Profile view - display info and all their posts
    - gets the primary key (pk) and check if it matches
    - filters posts to display only the one from this user
    - count how many followers this profile has
    - check if the current user is a follower with for loop
    """
    def get(self, request, pk, *args, **kwargs):
        """ display profile """
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        # followers handling:
        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
        }

        return render(request, 'core/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Profile edit """
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'core/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class AddFollower(LoginRequiredMixin, View):
    """ Adds a follower to the user profile """
    def post(self, request, pk, *args, **kwargs):
        """ the current user gets added to the list of followers  """
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)
        return redirect('profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    """ Remove follower from the user profile """
    def post(self, request, pk, *args, **kwargs):
        """ the current user gets removed to the list of followers  """
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        return redirect('profile', pk=profile.pk)


class AddLike(LoginRequiredMixin, View):
    """ User can like a post """
    def post(self, request, pk, *args, **kwargs):
        """ Like post, reverts if it was disliked before """
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        # return to the previous template
        next_value = request.POST.get('next', '/')
        return HttpResponseRedirect(next_value)


class AddDislike(LoginRequiredMixin, View):
    """ User can dislike a post, youtube style """
    def post(self, request, pk, *args, **kwargs):
        """ Dislike post, reverts if it was liked before """
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        # return to the previous template
        next_value = request.POST.get('next', '/')
        return HttpResponseRedirect(next_value)


class UserSearch(View):
    """ search for user profiles """
    def get(self, request, *args, **kwargs):
        """ get users and query for the selected characters """
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }

        return render(request, 'core/search.html', context)


class ListFollowers(View):
    """ Displays the followers that the user profile has """
    def get(self, request, pk, *args, **kwargs):
        """ gets followers """
        profile = UserProfile.objects.get(pk=pk)
        followers = profile.followers.all()

        context = {
            'profile': profile,
            'followers': followers,
        }

        return render(request, 'core/followers_list.html', context)


def error_404(request, exception):
    """ 404 error handler """
    return render(request, '404.html')
