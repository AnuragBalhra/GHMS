from django.http import HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import render

from user.models import *

def hello(request):
    return HttpResponse("Hello world")

def home(request):
	return render(request, 'includes/base.html', {'title':'GuestHouse Homepage'})

def login(request):
	
	#if request.POST['username'] and request.POST['password']:
		username=request.POST['username']
		password=request.POST['password']
		user=User.objects.filter(Name=username,Password=password)
		return HttpResponse('User Name %s %s .' %(user.Name, user.Password))
		# return render(request, 'profile.html', {'user':user})
	#else:
		return render(request, 'login.html', {'title':'GuestHouse Homepage'})
