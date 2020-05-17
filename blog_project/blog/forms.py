from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        # connect with a proper model claasss
        model = Post
        # connect the fields you'll be able to edit
        # why tuples here? because they're IMMUTABLE
        fields = ('author', 'title', 'text')


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')