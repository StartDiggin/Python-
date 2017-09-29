# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from models import *

#Route to index-> /pokes/
def index(request):

    context = {
    'curUser':User.objects.get(id = request.session['id']),
    'otherUser':User.objects.exclude(id = request.session['id']),
    'count': None,
    'numUser': None,
    'gotPoke':[],
    'whoPoke':[]
    }
    curUser = User.objects.get(id = request.session['id'])
    otherUser = User.objects.exclude(id = request.session['id'])

    for others in otherUser:
        context['whoPoke'].append(others)
    context['count'] = len(context['whoPoke'])


    return render(request,'pokes_app/index.html',context)

#Route to index-> /pokes/addpoke
def addpoke(request, id):
    curUser = User.objects.get(id = request.session['id'])
    otherUser = User.objects.get(id = id)
    return redirect('/pokes/')

#Route to logout-> /pokes/logout
def logout(request):
    request.session.flush()
    return redirect('/')
