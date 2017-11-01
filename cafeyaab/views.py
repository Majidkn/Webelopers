#!/usr/bin/python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
from .forms import SignUpForm


def BaseView(request):
    return render(request, 'cafeyaab/__base.html')


def HomeView(request):
    return render(request, 'cafeyaab/_home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.validation() == None:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            Form = SignUpForm()
            return render(request, 'cafeyaab/_signup.html',
                          {'form': Form, 'errors': form.validation()})
    else:
        form = SignUpForm()

    return render(request, 'cafeyaab/_signup.html', {'form': form})
