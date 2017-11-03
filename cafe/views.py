# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect

from cafeyaab.models import User as user
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Cafe, CafeImage, Comment

from django.shortcuts import render, redirect
import json
from .forms import CommentForm


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
        return render(request, 'cafes/_cafes.html', {'cafes': Cafe.objects.all().order_by('-popularity')})


def cafe(request, pk):
    commentForm = CommentForm()
    currnetCafe = Cafe.objects.get(id=pk)
    return render(request, 'cafes/_cafe.html',
                  {'cafe': currnetCafe, 'images': CafeImage.objects.filter(cafe=pk),
                   'commentForm': commentForm, 'comments': Comment.objects.filter(cafe=currnetCafe)})


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
            commentForm = CommentForm()
            return redirect('/cafes/' + str(pk))


def hideComment(request, cafeId, commentId):
    if request.user.is_superuser:
        comment_ = Comment.objects.get(id=commentId)
        comment_.show = False
        comment_.save()
        print (comment_.show)
        comment_.refresh_from_db()
        print (comment_.show, comment_.id)
        return redirect('/cafes/' + str(cafeId))
    else:
        return redirect('/cafes/' + str(cafeId))


def showComment(request, cafeId, commentId):
    if request.user.is_superuser:
        comment_ = Comment.objects.get(id=commentId)
        comment_.show = True
        comment_.save()
        comment_.refresh_from_db()
        return redirect('/cafes/' + str(cafeId))
    else:
        return redirect('/cafes/' + str(cafeId))


def favit(request, cafeid):
    print("Entered")
    user = request.user
    if user.fav_list.filter(id=cafeid).exists():
        user.fav_list.remove(get_object_or_404(Cafe, pk=cafeid))
        mycafe = Cafe.objects.get(pk=cafeid)
        mycafe.popularity -= 1
        mycafe.save()

    else:
        user.fav_list.add(get_object_or_404(Cafe, pk=cafeid))
        mycafe = Cafe.objects.get(pk=cafeid)
        mycafe.popularity += 1
        mycafe.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))