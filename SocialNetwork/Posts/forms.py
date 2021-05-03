from django import forms 
from .models import Post ,Comment

class PostsCreateForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
    
        'class':'form-control',
        'placeholder':' write post here !',
        'rows':1,
        'cols':20
    }))
    class Meta:
        model = Post
        fields="__all__"
        # widgets = {
        # 'user_id': forms.HiddenInput(),
        
        #  }
        
class CommentsCreateForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    
    class Meta:
        model=Comment
        fields ="__all__"
        widgets = {
        'post_id': forms.HiddenInput(),
        
         }
      
    

