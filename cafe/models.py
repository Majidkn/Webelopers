# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    main_image_url = models.URLField(default='300.png')
    creator = models.ForeignKey(User, null=True, blank=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CafeImage(models.Model):
    cafe = models.ForeignKey(to=Cafe, related_name='all_images')
    image_url = models.URLField()


class Comment(models.Model):
    text = models.TextField()
    cafe = models.ForeignKey(Cafe, null=True)
    author = models.ForeignKey(User)
    show = models.BooleanField(default=True)
