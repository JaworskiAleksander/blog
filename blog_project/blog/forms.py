from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        # connect with a proper model claasss
        model = Post
        # connect the fields you'll be able to edit
        # why tuples here? because they're IMMUTABLE
        fields = ('author', 'title', 'text')

        # adding widgets to mess with css later
        # all inside Meta class
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            # long class name, because later we'll be working with Medium text editor
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')