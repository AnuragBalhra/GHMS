from django.http import HttpResponseRedirect,HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect


from basic.user.user import User
from basic.administrator.administrator import Administrator
from basic.food import Food
from basic.booking import Booking
from basic.guestHouse import guestHouse
from basic.dataBase import dataBase


def hello(request):
    return HttpResponse("Hello world")

def home(request):
	return render(request, 'includes/base.html', {'title':'GuestHouse Homepage'})

def validate(request):
	
	try:
		user = request.session['visitor']
	except:
		return render(request, 'login.html', {'title':'GuestHouse Login'})

	if(isinstance(user, Administrator)):
		request.session['type']='admin'
	elif(isinstance(user, User)):
		request.session['type']='user'
	else:
		request.session['type']='visitor'

def profile(request):
			
	if(request.session['visitor']['type']=='admin'):
		admin=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		return render(request, 'admin/', {'admin':admin} )
	elif(request.session['visitor']['type']=='user'):
		return render(request, 'user/' )
	return redirect('login')

		


def home(request):
	return redirect('login')
	
	return render(request, 'includes/base.html', {'title':'GuestHouse Homepage'})


def login(request):
	# return HttpResponse("Hello world")
	# exit()
	try:
		if(request.session['logged_in']==True):
			request.session['err']="Already logged In"
			return HttpResponseRedirect('../'+request.session['visitor']['type']+'/')
	except:
		request.session['err']="Not already logged In"
		request.session['logged_in']=False
	

	if 'username' in request.POST and 'password' in request.POST and 'type' in request.POST:
		username=request.POST['username']
		password=request.POST['password']
		type=request.POST['type']
		
		user=User(username,password,type)
		try:
			if(user.login(username,password, type)!=True):
				request.session['err']="Check Username , password and role"
				return redirect('logout')
		except:
			request.session['err']="Check Username , password and role"
			return redirect('logout')

		if type=='admin':
			admin=get_object_or_404(Administrator, Name=username,Password=password)
			request.session['visitor']={}
			request.session['visitor']['Id']=admin.Id
			request.session['visitor']['type']='admin'
			request.session['logged_in']=True
			request.session['err']=""

			return HttpResponseRedirect('../admin/')
			# return HttpResponse('Admin Name %s %s %s .' %( admin.Id, admin.Name, admin.Password))
			return redirect('admin' )
		else:
			user=get_object_or_404(User, Name=username,Password=password)
			request.session['visitor']={}
			request.session['visitor']['Id']=user.Id
			request.session['visitor']['type']='user'
			request.session['logged_in']=True
			request.session['err']=""
			return HttpResponseRedirect('../user/')
			# return redirect('user' )
	else:
		# return HttpResponse("Hello world")
		# exit()
		# request.session['logged_in']=False
		err=request.session['err']
		request.session['err']=""
		# exit()
		return render(request, 'login.html', {'title':'GuestHouse Login', 'err':err})

def logout(request):
	request.session['logged_in']=False
	try:
		del request.session['visitor']
		request.session.flush()
		request.session['err']="Successfully logged out"
		request.session['logged_in']=False

	except:
		pass
	return redirect('login')

