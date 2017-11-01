# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cafe, CafeImage

# Register your models here.

admin.site.register(Cafe)
admin.site.register(CafeImage)
