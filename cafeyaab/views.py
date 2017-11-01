# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def BaseView(request):
    return render(request, 'cafeyaab/__base.html')


def HomeView(request):
    return render(request, 'cafeyaab/_home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'cafeyaab/_signup.html', {'form': form})
