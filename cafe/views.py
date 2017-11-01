# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Cafe

from django.shortcuts import render


def cafes(request):
    if request.GET.get('query'):
        return render(request, 'cafes/_cafes.html', {'cafes': Cafe.objects.filter(name__contains=request.GET.get('query'))})
    else:
        return render(request, 'cafes/_cafes.html', {'cafes': Cafe.objects.all()})


def cafe(request, pk):
    return render(request, 'cafes/_cafe.html', {'cafe': Cafe.objects.get(id=pk)})
