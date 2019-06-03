from django.http import HttpResponse
from django.shortcuts import render
from pril import models
from pril.models import Collect,Template
from userpr.models import Userpr
from django.http import HttpResponse


def index(request):
    return render (request,'base.html')


def meetings_list(request):
    col_list = Collect.objects.all()
    context = {'col_list': col_list}
    return render(request, 'collect.html', context)

def user_list(request):
    usarsi = Userpr.objects.filter(user=request.user)
    context = {'usarsi':usarsi}
    return render(request,'collect.html',context)

def viev_profile (request):
    args ={'user': request.user}
    return render(request,'collect.html',args)


def template_sobr(request):
    templ_list = Template.objects.all()
    context = {'templ_list':templ_list}
    return render(request, 'templat.html', context)