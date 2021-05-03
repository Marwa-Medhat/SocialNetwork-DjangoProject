from django import forms 
from .models import Post

class PostsCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields="__all__"
        #fields=['content','post_image','Group_id','user_id']

