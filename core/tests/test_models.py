""" Imports """
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Post, Comment, UserProfile


class TestModels(TestCase):
    """ Models testing """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john',
            'lennon@thebeatles.com',
            'johnpassword'
            )
        self.client.login(username='john', password='johnpassword')
        self.post = Post.objects.create(
            body='text',
            created_on=timezone.now(),
            author=self.user,
        )
        self.comment = Comment.objects.create(
            comment='some random comment',
            created_on=timezone.now(),
            author=self.user,
            post=self.post,
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            name='john',
            bio='beatles member',
            birth_date=timezone.now(),
            location='London, UK',
        )

    # Post model tests:
    def post_user_is_correct(self):
        """ Test if post's user is assigned correctly """
        self.assertEqual(self.post.author, self.user)

    def post_has_a_timestamp(self):
        """ Test if post has a date of creation """
        self.assertNotEqual(self.post.created_on, '')

    def post_has_body(self):
        """ Test if post is not empty """
        self.assertNotEqual(self.post.body, '')
        self.assertEqual(self.post.body, 'text')

    # Comment model tests
    def comment_user_is_correct(self):
        """ Test if comment's user is assigned correctly """
        self.assertEqual(self.comment.author, self.user)

    def comment_has_a_timestamp(self):
        """ Test if comment has a date of creation """
        self.assertNotEqual(self.comment.created_on, '')

    def comment_has_body(self):
        """ Test if comment is not empty """
        self.assertNotEqual(self.comment.body, '')
        self.assertEqual(self.comment.body, 'some random comment')

    # UserProfile model tests:
    def user_profile_has_picture(self):
        """ Test if profile has default picture even if not setup """
        self.assertEqual(self.user_profile.picture.count(), 1)

    def user_profile_has_followers_field(self):
        """ Test if user profile has followers field """
        self.assertEqual(self.user_profile.followers.count(), 0)
