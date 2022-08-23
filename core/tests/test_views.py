""" Imports: """
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Post, Comment, UserProfile
import json


class TestViews(TestCase):
    """ views tests """

    def setUp(self):
        self.post = Post()

    def test_post_list_view_get(self):
        """ tests that response for GET is positive """
        response = self.post.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/post_list.html')
