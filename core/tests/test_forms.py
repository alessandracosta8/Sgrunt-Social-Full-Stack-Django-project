""" Imports """
from django.test import SimpleTestCase
from core.forms import PostForm, CommentForm


class TestForms(SimpleTestCase):
    """ Forms testing """

    def setUp(self):
        self.form = PostForm(
            data={
                'body': 'Some text that will be the body of the post.'
            }
        )
        self.comment = CommentForm(
            data={
                'comment': 'A random comment.'
            }
        )

    # PostForm tests:
    def test_post_form_valid_data(self):
        """ tests PostForm contains valid data """
        self.assertTrue(self.form.is_valid())

    def test_post_form_no_data(self):
        """ tests PostForm is not valid when empty """
        self.form = PostForm(data={})
        self.assertFalse(self.form.is_valid())
        self.assertEqual(len(self.form.errors), 1)

    # CommentForm tests:
    def test_comment_form_valid_data(self):
        """ tests CommentForm contains valid data """
        self.assertTrue(self.comment.is_valid())

    def test_comment_form_no_data(self):
        """ tests CommentForm is not valid when empty """
        self.form = CommentForm(data={})
        self.assertFalse(self.comment.is_valid())
        self.assertEqual(len(self.comment.errors), 1)
