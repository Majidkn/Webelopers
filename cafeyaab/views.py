#!/usr/bin/python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
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
            user.is_active = False
            user.save()
    else:
        form = SignUpForm()
    return render(request, 'cafeyaab/_signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'cafeyaab/account_activation_sent.html')
