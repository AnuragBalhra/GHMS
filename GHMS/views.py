from django.http import HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect

from user.models import *

import '../assets/py/header.py'
def hello(request):
    return HttpResponse("Hello world")

def home(request):
	return render(request, 'includes/base.html', {'title':'GuestHouse Homepage'})

def validate(request):
	
	try:
		user = request.session['visitor']
	except:
		return render(request, 'login.html', {'title':'GuestHouse Login'})

	if(isinstance(user, Admin)):
		request.session['type']='admin'
	elif(isinstance(user, User)):
		request.session['type']='user'
	else:
		request.session['type']='visitor'

def profile(request):
	return render(request, 'profile.html' )
	


def home(request):
	
	return render(request, 'includes/base.html', {'title':'GuestHouse Homepage'})


def login(request):
    # return HttpResponse("Hello world")
	try:
		if(request.session['logged_in']):
			return redirect('profile')
	except:
		request.session['logged_in']=False
	if 'username' in request.POST and 'password' in request.POST and 'type' in request.POST:
		username=request.POST['username']
		password=request.POST['password']
		type=request.POST['type']
		
		if type=='admin':
			admin=get_object_or_404(Admin, Name=username,Password=password)
			user=admin
			request.session['visitor']=user
			request.session['logged_in']=True
			# return HttpResponse('Admin Name %s %s %s .' %( admin.Id, admin.Name, admin.Password))
			return redirect('profile')
		else:
			user=get_object_or_404(User, Name=username,Password=password)
			request.session['visitor']=user
			request.session['logged_in']=True
			return render(request, 'profile.html', {'user':user})
	else:
		request.session['logged_in']=False
		return render(request, 'login.html', {'title':'GuestHouse Login'})
