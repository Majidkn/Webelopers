#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(help_text=u"(اجباری)", max_length=30, required=True, label=u"نام")
    username = forms.CharField(help_text=u"(اجباری)", max_length=50, required=True, label=u"نام‌کاربری")
    email = forms.EmailField(help_text=u"(اجباری)", max_length=254, required=True, label=u"ایمیل")
    password1 = forms.CharField(help_text=u"(اجباری)", label=u"رمزعبور", widget=forms.PasswordInput)
    password2 = forms.CharField(help_text=u"(اجباری)", label=u"تایید رمزعبور", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2',)

    # def validation(self):
    #     if(objectself.username)