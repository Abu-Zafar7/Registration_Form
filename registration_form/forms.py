from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),help_text=UserCreationForm().fields['username'].help_text)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),help_text=UserCreationForm().fields['password1'].help_text)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),help_text=UserCreationForm().fields['password2'].help_text)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
      



   