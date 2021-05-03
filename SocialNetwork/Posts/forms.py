from django import forms
from .models import Post


class PostsCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # exclude = ('user_id',)  # ETA: added comma to make this a tuple
        # widgets = {
        #     'user_id': forms.HiddenInput(),
        # }
