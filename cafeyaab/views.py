#!/usr/bin/python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse

from cafeyaab.forms import EditForm
from .forms import SignUpForm


def BaseView(request):
    return render(request, 'cafeyaab/__base.html')


def HomeView(request):
    return render(request, 'cafeyaab/_home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'cafeyaab/_signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'cafeyaab/account_activation_sent.html')


def delete_image(request, userId):
    user.profile_pic = 'pic_folder/__none/no-img.png'
    user.save()
    return redirect('profile')


def profile(request):

    if request.user.is_authenticated:
        return render(request, 'cafeyaab/profile.html')
    else:
        return redirect('login')


def editprofile(request):
    if request.method == 'POST':
        form = EditForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            print(user.profile_pic.url)
            user.save()
            return redirect('profile')
    else:

        form = EditForm(instance=request.user)

    return render(request, 'cafeyaab/editprofile.html', {'form': form, 'userId':request.user.id})