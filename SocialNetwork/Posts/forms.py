from django import forms 
from .models import Post , Comment


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
        exclude = ['user_id','likes']
        
        
class CommentsCreateForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control rounded-pill',
        'placeholder':'Comment here !',
        'rows':2,
        'cols':10,
        
    }))
    
    class Meta:
        model=Comment
        fields ="__all__"
        exclude = ['user'] #b3t bdlha kima 
        widgets = {
        'post_id': forms.HiddenInput(),
        
        }
        # bi5fy el field men 8air ma ab3t kima 
      
    

