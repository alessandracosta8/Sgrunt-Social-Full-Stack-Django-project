"""
Imports:
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """
    Post model:
    - body is text
    - created_on will be setup on time and date when submit button is hit
    - author setup with cascade so if User is deleted, so are their posts
    - likes and dislikes collected
    - post images linked
    """
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)


class Comment(models.Model):
    """ Comment model """
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class UserProfile(models.Model):
    """
    User Profile model
    - One to one field -> A user can have only one profile and viceversa
    - Field to store followers
    """
    user = models.OneToOneField(
        User,
        primary_key=True,
        verbose_name='user',
        related_name='profile',
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(
        upload_to='uploads/profile_pictures',
        default='uploads/profile_pictures/default.png',
        blank=True
        )
    followers = models.ManyToManyField(
        User,
        blank=True,
        related_name='followers'
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
