# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cafe, CafeImage, Comment

# Register your models here.

admin.site.register(Cafe)
admin.site.register(CafeImage)
admin.site.register(Comment)
