from django import forms
from blog.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text') # field that need to be showed in the form
        # assign field to medium editor library
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text') # field that need to be showed in the form
        # assign field to medium editor library
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
