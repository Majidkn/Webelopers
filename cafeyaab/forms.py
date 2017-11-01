from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, label=u"سلام")
    username = forms.EmailField(max_length=50, required=True, )
    email = forms.EmailField(max_length=254, required=True, label="ایمیل")
    password1 = forms.CharField(help_text="", label="رمزعبور")
    password2 = forms.CharField(help_text="", label="تایید رمزعبور")

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2',)
