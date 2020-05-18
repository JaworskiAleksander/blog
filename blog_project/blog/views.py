# django imports
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


# blog app import
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

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

# function based view - import login_required from django.contrib.auth.decorators
# class-based views - import LoginRequiredMixin from django.contrib.auth.mixins
class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post

    # defining attributes from LoginRequiredMixins
    # when user is not logged in, and wants to use this view, redirect them here:
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    persmission_denied_message = 'YOU SHALL NOT POST HERE!'

    # from django doc: https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class
    # The form class HAS TO instantiate
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # defining values of atributes that come from LoginRequiredMixin class
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    persmission_denied_message = 'YOU HAVE NO POWER HERE!'

    # defining values of atributes that come from UpdateView class
    model = Post
    # attributes for Create and Update are the same, and it makes sense

class PostDeleteView(LoginRequiredMixin, DeleteView):
    pass

# all posts, before publishing, are labeled as drafts, thus this view is also necessary
# class Drafts()