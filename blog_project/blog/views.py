# django imports
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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
    permission_denied_message = 'YOU SHALL NOT POST HERE!'

    # from django doc: https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class
    # The form class HAS TO instantiate
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # defining values of atributes that come from LoginRequiredMixin class
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    permission_denied_message = 'YOU HAVE NO POWER HERE!'

    # defining values of atributes that come from UpdateView class
    model = Post
    # attributes for Create and Update are the same, and it makes sense

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # revrse_lazy is activated AFTER the action is completed, which makes it safe to use here
    # once a post is successfuly deleted, let's go to homepage
    success_url = reverse_lazy('post_list')
    

    pass

# all posts, before publishing, are labeled as drafts, thus this view is also necessary
class Drafts(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/drafts.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date')


#----------------------------------------
# Drafts

@login_required(login_url='login')
def add_comment_to_post(request, pk):
    # either get the Post object from dataase, with an id=pk, or return 404
    post = get_object_or_404(Post, pk=pk)
    # if someone filled in the form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required(login_url='login')
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required(login_url='login')
def comment_remove(request, pk):
    # get the Comment object with id = pk, return 404 if not found
    comment = get_object_or_404(Comment, pk=pk)
    # save post.pk it was attached to, we'll use it later, after the comment is deleted
    post_pk = comment.post.pk
    # delete the comment
    comment.delete()
    # return to the page this comment was attached to
    return redirect('post_detail', pk=post_pk)

    pass