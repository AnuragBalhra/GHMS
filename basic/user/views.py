from django.http import HttpResponseRedirect,HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect



from basic.user import *
from basic.admin import *
from basic.food import *
from basic.booking import *
from basic.guestHouse import *
from basic.dataBase import *


# Create your views here.


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

	return render(request, 'user/profile.html',{'visitor':visitor,'all_bookings':all_bookings})
    # return HttpResponse("User Hello world")



def search(request):
	visitor=get_object_or_404(User, Id=request.session['visitor']['id'])
	obj=visitor.searchRoom(request.POST['checkIn'], request.POST['checkOut'])
	try:
		if(isinstance(obj, Booking)):
			return redirect('showBooking')
			
		return showRooms(obj)
	except:
		return showRooms(obj)

	# return HttpResponse(available_rooms)

def showBooking(booking):
	raise Exception(booking)


def showRooms(available_rooms):
	raise Exception(available_rooms)

