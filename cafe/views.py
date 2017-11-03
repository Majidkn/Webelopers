# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import user
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from cafeyaab.models import User as user
from cafeyaab.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Cafe, CafeImage, Comment

from django.shortcuts import render, redirect
import json
from .forms import CommentForm


def get_cafes(request):
    results = []
    if request.is_ajax():
        cafes = Cafe.objects.filter(name__contains=request.GET.get('term'), activated=True)[:20]
        for cafe in cafes:
            results.append(cafe.name)

        data = json.dumps(results)
    else:
        data = 'fail'
    return HttpResponse(data)


def cafes(request):
    if request.GET.get('query'):
        return render(request, 'cafes/_cafes.html',
                      {'cafes': Cafe.objects.filter(name__contains=request.GET.get('query'), activated=True),
                       'query': request.GET.get('query')})
    else:
        return render(request, 'cafes/_cafes.html', {'cafes': Cafe.objects.filter(activated=True)})


def cafe(request, pk):
    comment_form = CommentForm()
    current_cafe = Cafe.objects.get(id=pk)
    return render(request, 'cafes/_cafe.html',
                  {'cafe': current_cafe, 'images': CafeImage.objects.filter(cafe=pk),
                   'comment_form': comment_form, 'comments': Comment.objects.filter(cafe=current_cafe)})


def comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.cafe = Cafe.objects.get(id=pk)
            comment.author = User.objects.get(id=request.user.id)
            comment.save()
            return redirect('/cafes/' + str(pk))

        else:
            return redirect('/cafes/' + str(pk))


def change_comment_visibility(request, cafe_id, comment_id):
    if request.user.is_superuser:
        comment_ = Comment.objects.get(id=comment_id)
        comment_.show = not comment_.show
        comment_.save()
        comment_.refresh_from_db()
        return redirect('/cafes/' + str(cafe_id))
    else:
        return redirect('/cafes/' + str(cafe_id))


def favourite(request, cafe_id):
    current_user = request.user
    if current_user.fav_list.filter(id=cafe_id).exists():
        current_user.fav_list.remove(get_object_or_404(Cafe, pk=cafe_id))
        cafe_to_change = Cafe.objects.get(pk=cafe_id)
        cafe_to_change.popularity -= 1
        cafe_to_change.save()

    else:
        current_user.fav_list.add(get_object_or_404(Cafe, pk=cafe_id))
        cafe_to_change = Cafe.objects.get(pk=cafe_id)
        cafe_to_change.popularity += 1
        cafe_to_change.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
