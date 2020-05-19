from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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

    def get_absolute_url(self):
        # after the psot is created, go to post_detail.html
        # with index of self.pk
        return reverse("post_detail", kwargs={"pk": self.pk})
    


class Comment(models.Model):
    # each comment is related to an instance of blog.Post class
    # it's connected via 'comments' alias
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
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

    def __str__(self):
        return self.text

    # since a comment has to be approved first, before it can be viewed, it doens't make sense
    # to go see it after commenting
    # lets go to post page and display message
    # 'comment added, awaiting for approval'
    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})