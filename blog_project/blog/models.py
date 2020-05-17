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

    def publish(self):
        # set the time post is published
        self.published_date = timezone.now()
        # save the change into database
        self.save()

    def approve_comments(self):
        # only approved comments will be displayed
        # this method is how you change that attribute
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title[:25]


class Comment(models.Model):
    # each comment is related to an instance of blog.Post class
    # it's connected via 'comments' alias
    post = models.ForeignKey('blog.Post', related_name='comments')
    # who's the author
    author = models.CharField(max_length=256)
    # message
    text = models.TextField(max_length=512)
    # comment creation date, default is now(), no user has no access to this field
    create_date = models.DateTimeField(default=timezone.now())
    # by default comment is not approved, only admin can change this field
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()


