from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from blog.models import Post, Comment
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # this allows to use django ORL
    def get_queryset(self):
        # get all objects whose published_date field is less than or equal to timezone.now()
        # and filter it by publish_date field in descending order
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post