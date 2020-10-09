from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-inp'}))
    first_name = forms.CharField(
        max_length=30, required=False, help_text="Optional.", widget=forms.TextInput(attrs={'class': 'form-inp'}))
    last_name = forms.CharField(
        max_length=30,  required=False, help_text="Optional.", widget=forms.TextInput(attrs={'class': 'form-inp'}))
    email = forms.EmailField(
        max_length=254, help_text="Required. Inform a valid email address", widget=forms.EmailInput(attrs={'class': 'form-inp'}))
    address = forms.CharField(
        max_length=254,  required=False, help_text="Optional.", widget=forms.Textarea(attrs={'class': 'form-textarea'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-inp'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-inp'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'email', 'address',)
