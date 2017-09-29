# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
import calendar

# Create your views here.
def index(request):
    # User.objects.all().delete()
    return render(request,'login_app/index.html')

def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, 'User created')
        return redirect('/dashboard')
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'check email and password')
        return redirect('/')
    request.session['first_name'] = results['user'].first_name
    request.session['last_name'] = results['user'].last_name
    request.session['email'] = results['user'].email
    request.session['id'] = results['user'].id
    return redirect('/pokes/')

def dashboard(request):
    if 'email' not in request.session:
        return redirect('/')
    return render(request, 'login_app/dashboard.html')

def logout(request):
    request.session.flush()
    return redirect('/')
