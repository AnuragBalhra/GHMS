from django.http import HttpResponseRedirect,HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.


from basic.user import *
from basic.admin import *
from basic.food import *
from basic.booking import *
from basic.guestHouse import *
from basic.dataBase import *


def dashboard(request):
	if request.session['visitor']['type']=='admin':
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['id'])
		try:
			all_bookings=DBMS.getBookings('admin')
		except:
			all_bookings=None

	else:
		visitor=get_object_or_404(User, Id=request.session['visitor']['id'])
		try:
			all_bookings=DBMS.getBookings('user', visitor)
		except:
			all_bookings=None

	return render(request, 'admin/profile.html',{'visitor':visitor,'all_bookings':all_bookings})