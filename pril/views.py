from django.http import HttpResponse
from django.shortcuts import render
from pril import models
from pril.models import Collect,Template
from userpr.models import Userpr


def index(request):
    return render (request, "base.html")


def meetings_list(request):
    col_list = Collect.objects.all()
    context = {'col_list': col_list}
    return render(request, 'collect.html', context)

def user_list(request):
    usar = Userpr.objects.all()
    context = {'usar':usar}
    return render(request,'collect.html',context)


def template_sobr(request):
    templ_list = Template.objects.all()
    context = {'templ_list':templ_list}
    return render(request, 'templat.html', context)