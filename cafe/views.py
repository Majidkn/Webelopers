# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from .models import Cafe, CafeImage

from django.shortcuts import render
import json


def get_cafes(request):
    results = []
    if request.is_ajax():
        cafes = Cafe.objects.filter(name__contains=request.GET.get('term'))[:20]
        for cafe in cafes:
            results.append(cafe.name)

        data = json.dumps(results)
    else:
        data = 'fail'
    return HttpResponse(data)


def cafes(request):
    if request.GET.get('query'):
        return render(request, 'cafes/_cafes.html',
                      {'cafes': Cafe.objects.filter(name__contains=request.GET.get('query')),
                       'query': request.GET.get('query')})
    else:
        return render(request, 'cafes/_cafes.html', {'cafes': Cafe.objects.all()})


def cafe(request, pk):
    return render(request, 'cafes/_cafe.html',
                  {'cafe': Cafe.objects.get(id=pk), 'images': CafeImage.objects.filter(cafe=pk)})
