""" Imports """
from django.test import SimpleTestCase
from core.forms import PostForm, CommentForm


class TestForms(SimpleTestCase):
    """ Forms testing """

    # PostForm tests:
    def test_post_form_valid_data(self):
        """ tests PostForm contains valid data """
        form = PostForm(
            data={
                'body': 'Some text that will be the body of the post.'
            }
        )
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        """ tests PostForm is not valid when empty """
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    # CommentForm tests:
    def test_comment_form_valid_data(self):
        """ tests CommentForm contains valid data """
        comment = CommentForm(
            data={
                'comment': 'A random comment.'
            }
        )
        self.assertTrue(comment.is_valid())

    def test_comment_form_no_data(self):
        """ tests CommentForm is not valid when empty """
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
