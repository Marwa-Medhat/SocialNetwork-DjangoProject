from django import forms 
from .models import Group


class GroupsCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields="__all__"  
        exclude = ('members','owner',)      