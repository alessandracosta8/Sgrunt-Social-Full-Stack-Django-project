"""
Imports:
- base models
- timezone
- User model
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model:
    - body is text
    - created_on will be setup on time and date when submit button is hit
    - author setup with cascade so if User is deleted, so are their posts
    """
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
