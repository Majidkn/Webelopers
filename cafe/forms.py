#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.forms import ModelForm

from .models import Comment
from .models import Cafe


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


# class AddCafeForm(ModelForm):
#     class Meta:
#         model = Cafe
#         fields = ('name', 'description', 'latitude', 'longitude', 'main_image_url')
