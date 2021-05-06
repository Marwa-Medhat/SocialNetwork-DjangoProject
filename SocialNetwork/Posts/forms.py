from django import forms 
from .models import Post , Comment
from django.core.exceptions import ValidationError


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
        widgets = {
        'Group_id': forms.HiddenInput(),
         }
       


class AdminPostsCreateForm(forms.ModelForm):
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


    # def clean_content(self):
    #     content = self.cleaned_data.get("content")
    #     if "test" in content:
    #         raise ValidationError("title shouldn't has test word!")
    #     #####raise error?????


  # bi5fy el field men 8air ma ab3t kima 



class CommentsAdminEditForm(forms.ModelForm):
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
        widgets = {
           'user' :forms.HiddenInput(),
           'post_id' :forms.HiddenInput(),
         }
      

class CommentsAdminCreateForm(forms.ModelForm):
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
        
        # exclude = ['user']
        widgets = {
        #    'user' :forms.HiddenInput(),
        
         }
      

      
    
