from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    # charfield is for short messages
    title = models.CharField(max_length=200)
    # textield is for long messages
    text = models.TextField()
    # when the post is created, set up automaticaly, user can't modify it
    create_date = models.DateTimeField(default=timezone.now())
    # when the post is publicated on the wall, user chan choose when to publish their post
    published_date = models.DateTimeField(blank=True, null=True)
    # this set up allow for creating posts in advance, and posting them in a specific order
    # or when the user is offline and a post is scheduled at that time
    # what's the difference between blank and null? RTFM, FFS
    