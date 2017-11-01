# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView


def BaseView(request):
    return render(request, 'cafeyaab/base.html')


def HomeView(request):
    return render(request, 'cafeyaab/home.html')
