from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.http import response
import json


from django.http import HttpResponse
from django.views import View
from userpr.models import Userpr

def logowanie(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('id_username', '').strip(),
            password= request.POST.get('id_password', ''),
            )
        if user is None:
            messages.error(request, u'Invalid credentblog.ials')
        else:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
            else:
                messages.error(request, u'User is not active.')

                return render_to_response('registration/login.html', locals(),
                    context_instance=RequestContext(request))