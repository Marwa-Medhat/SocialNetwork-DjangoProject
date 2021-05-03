from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Users.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address.')
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    # gender = forms.CharField(
    #     choices=[('male', 'male'), ('female', 'female')], max_length=50)

    class Meta:
        model = CustomUser
        # ' gender'
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
