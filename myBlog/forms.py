from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Posts, Category

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", 'email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    class Meta():
        model = Posts
        fields = '__all__'

class CategoryForm(froms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'