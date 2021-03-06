# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from cafeyaab.models import User


# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    activated = models.BooleanField(default=False)
    main_image_url = models.URLField()
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CafeImage(models.Model):
    cafe = models.ForeignKey(to=Cafe, related_name='all_images')
    image_url = models.URLField()


class Comment(models.Model):
    text = models.TextField()
    cafe = models.ForeignKey(Cafe, null=True)
    show = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
