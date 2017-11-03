# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from cafe.models import Cafe


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/__none/no-img.png')
    fav_list = models.ManyToManyField(Cafe, default=None)


