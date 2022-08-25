""" Imports: """
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from core.models import Post, Comment


class TestViews(TestCase):
    """ views tests """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
            )
        # tests if user login works before running other tests
        self.client.login(username='john', password='johnpassword')
        self.post = Post.objects.create(
            body='text',
            created_on=timezone.now(),
            author=self.user,
        )
        self.list_url = reverse('post-list')
        self.detail_url = reverse('post-detail', args=['1'])
        self.edit_url = reverse('post-edit', args=['1'])
        self.profile_url = reverse('profile', args=['1'])
        self.profile_edit_url = reverse('profile-edit', args=['1'])
        self.post_delete_url = reverse('post-delete', args=['1'])
        self.comment_delete_url = reverse('comment-delete', args=['1', '1'])
        self.add_follower_url = reverse('add-follower', args=['1'])
        self.remove_follower_url = reverse('remove-follower', args=['1'])

    # PostListView tests:
    def test_post_list_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_list.html')

    def test_post_list_view_post(self):
        """ tests that response for POST is positive """
        response = self.client.post(
            self.list_url,
            {
                'body': 'new random post',
                'created_on': timezone.now(),
                'author': self.user,
            },
        )
        self.assertEqual(response.status_code, 200)

    # PostDetailView tests:
    def test_post_detail_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_detail.html')

    def test_post_detail_view_post(self):
        """ tests that response for POST is positive """
        response = self.client.post(
            self.detail_url,
            {
                'comment': 'some random comment',
                'created_on': timezone.now(),
                'author': self.user,
                'post': self.post,
            },
        )
        self.assertEqual(response.status_code, 200)

    # PostEditView tests:
    def test_post_edit_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_edit.html')

    def test_post_edit_view_post(self):
        """ tests that response for POST is positive """
        response = self.client.post(
            self.edit_url,
            {
                'body': 'new edited post',
                'created_on': timezone.now(),
                'author': self.user,
            },
        )
        self.assertEqual(response.status_code, 302)

    # PostDeleteView tests:
    def test_post_delete_view(self):
        """ test if post gets deleted """
        Post.objects.create(
            body='post that will be deleted',
            created_on=timezone.now(),
            author=self.user,
        )
        response = self.client.delete(
            self.post_delete_url,
        )
        self.assertEqual(response.status_code, 302)

    # Comment DeleteView tests:
    def test_comment_delete_view(self):
        """ test if comment gets deleted """
        Comment.objects.create(
            comment='some random comment',
            created_on=timezone.now(),
            author=self.user,
            post=self.post,
        )
        response = self.client.delete(
            self.comment_delete_url,
        )
        self.assertEqual(response.status_code, 302)

    # ProfileView tests:
    def test_profile_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profile.html')

    # ProfileEditView tests:
    def test_profile_edit_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.profile_edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/profile_edit.html')

    # AddFollower view tests:
    def test_add_follower_view_post(self):
        """ tests that response for POST is positive """
        response = self.client.post(self.add_follower_url)
        self.assertEqual(response.status_code, 302)

    # RemoveFollower view tests:
    def test_remove_follower_view_post(self):
        """ tests that response for POST is positive """
        response = self.client.post(self.remove_follower_url)
        self.assertEqual(response.status_code, 302)
