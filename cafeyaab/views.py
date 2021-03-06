#!/usr/bin/python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from cafe.models import Cafe
from .models import User
from cafeyaab.forms import EditForm
from .forms import SignUpForm
from django.http import JsonResponse

def BaseView(request):
    return render(request, 'cafeyaab/__base.html')


def HomeView(request):
    if request.user.is_authenticated:
        return redirect('cafes')
    else:
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_ = form.save(commit=False)
            user_.is_active = True
            user_.save()
            created_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'])
            login(request, created_user)
            return redirect('profile')
    else:
        form = SignUpForm()
        return render(request, 'cafeyaab/_signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'cafeyaab/account_activation_sent.html')


def delete_image(request, userId):
    user = User.objects.get(id=userId)
    user.profile_pic = 'pic_folder/__none/no-img.png'
    user.save()
    return redirect('profile')


def profiles(request, pk):
    current_profile = get_object_or_404(User, username=pk)
    if profile:
        return render(request, 'cafeyaab/profiles.html', {'profile': current_profile})
    else:
        return render(request, 'cafes/_cafes.html')


def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        cafes = Cafe.objects.filter(creator=user)
        print cafes
        if cafes:
            return render(request, 'cafeyaab/profile.html', {'cafes': cafes})
        else:
            return render(request, 'cafeyaab/profile.html', {'cafes': {}})
    else:
        return redirect('login')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditForm(data=request.POST, files=request.FILES, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return redirect('profile')
        else:
            form = EditForm(instance=request.user)
            return render(request, 'cafeyaab/edit_profile.html', {'form': form, 'userId': request.user.id})
    else:
        return redirect('login')


def add_cafe(request):
    if request.method == 'POST':
        tmp_cafe = request.POST
        new_cafe = Cafe()
        new_cafe.name = tmp_cafe['name']
        new_cafe.description = tmp_cafe['description']
        new_cafe.main_image_url = tmp_cafe['main_image_url']
        new_cafe.latitude = tmp_cafe['latitude']
        new_cafe.longitude = tmp_cafe['longitude']
        new_cafe.creator = User.objects.get(id=request.user.id)
        new_cafe.save()
        return redirect('/profile')

    else:
        return render(request, 'cafes/_add_cafe.html')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)