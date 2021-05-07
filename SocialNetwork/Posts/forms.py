from django import forms 
from .models import Post , Comment, BadWords
from django.core.exceptions import ValidationError
from django.core import serializers



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

        exclude = ['user_id', 'Group_id', 'likes']

        widgets = {
        'Group_id': forms.HiddenInput(),
         }
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        words_list = serializers.serialize("python", BadWords.objects.all())
        for word in words_list:
            for field_name, field_value in word['fields'].items():
                print (field_name,'->', field_value ,type(field_name))
                print()
                if field_value in content:
                  raise ValidationError("Your post contains inappropriate words! , you cant use "+ field_value)
        return content



    
        
        
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


    def clean_content(self):
        content = self.cleaned_data.get("content")
        words_list = serializers.serialize("python", BadWords.objects.all())
        for word in words_list:
            for field_name, field_value in word['fields'].items():
                print (field_name,'->', field_value ,type(field_name))
                print()
                if field_value in content:
                  raise ValidationError("Your comment contains inappropriate words! , you cant use"+ field_value)
        return content


  # bi5fy el field men 8air ma ab3t kima 


class BadwordsCreateForm(forms.ModelForm):
        class Meta:
            model=BadWords
            fields ="__all__"