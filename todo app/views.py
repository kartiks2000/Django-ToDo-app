# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from todoapp.models import todoitem

# Create your views here.

def index(request):
    myl = todoitem.objects.all()
    return render(request,"home.html",context={'mylist' : myl})


def add(request):
     c = request.POST['newt']
     t = todoitem(task=c)
     t.save()
     return HttpResponseRedirect('/home/')


def delete(request,myid):
    print(myid)
    c = todoitem.objects.get(id=myid)
    c.delete()
    return HttpResponseRedirect('/home/')


