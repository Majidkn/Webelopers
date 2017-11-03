#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms
from django.contrib.auth.forms import UserCreationForm
from cafeyaab.models import User
from captcha.fields import CaptchaField
from django.forms.models import ModelForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='Name')
    email = forms.EmailField(max_length=254, help_text='Required.')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput, )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', 'captcha')


class EditForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label='Name')
    email = forms.EmailField(max_length=254, help_text='Required.')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2', 'profile_pic')