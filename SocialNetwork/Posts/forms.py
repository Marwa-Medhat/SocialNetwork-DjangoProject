from django import forms 
from .models import Post

class PostsCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields="__all__"
