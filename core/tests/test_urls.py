""" Imports: """
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import (
    PostListView,
    PostDetailView,
    PostEditView,
    PostDeleteView,
    CommentDeleteView,
    ProfileView,
    ProfileEditView,
    AddFollower,
    RemoveFollower
)


class TestUrls(SimpleTestCase):
    """ core app urls testing """

    def test_post_list_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('post-list')
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_post_detail_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('post-detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_post_edit_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('post-edit', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PostEditView)

    def test_post_delete_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('post-delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    def test_comment_delete_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('comment-delete', args=['1', '1'])
        self.assertEqual(resolve(url).func.view_class, CommentDeleteView)

    def test_profile_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('profile', args=['1'])
        self.assertEqual(resolve(url).func.view_class, ProfileView)

    def test_profile_edit_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('profile-edit', args=['1'])
        self.assertEqual(resolve(url).func.view_class, ProfileEditView)

    def test_add_follower_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('add-follower', args=['1'])
        self.assertEqual(resolve(url).func.view_class, AddFollower)

    def test_remove_follower_url_is_resolved(self):
        """ check if url calls the right view """
        url = reverse('remove-follower', args=['1'])
        self.assertEqual(resolve(url).func.view_class, RemoveFollower)
