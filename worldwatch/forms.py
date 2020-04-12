from django import forms
from worldwatch.models import Profile, Comments
from django.contrib.auth.forms import AuthenticationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'age']

class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['comment']