""" Imports: """
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Post, Comment, UserProfile
from model_bakery import baker


class TestViews(TestCase):
    """ views tests """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
            )
        self.client.login(username='john', password='johnpassword')
        self.post = baker.make(Post)
        self.list_url = reverse('post-list')
        self.detail_url = reverse('post-detail', args=['1'])

    def test_post_list_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_list.html')

    def test_post_detail_view_get(self):
        """ tests that response for GET is positive """
        response = self.client.get(self.detail_url)
        self.assertTemplateUsed(response, 'core/post_detail.html')
