from django.http import HttpResponseRedirect,HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect
import datetime
# from django.db import connections, transaction
from django.core.cache import cache



from basic.user import *
from basic.admin import *
from basic.food import *
from basic.booking import *
from basic.guestHouse import *
from basic.dataBase import *


# Create your views here.


def dashboard(request):						# view to show User Profile
	try:									# checking if any error occurs in session
		if(request.session['err']!=""):
			err=request.session['err']		# if error exists then capture and delete the error
			del request.session['err']
		else:
			raise Exception("No Error")
	except:
		err=""								# remove any preceding errors

	try:
		if request.session['visitor']['type']=='admin':				
			visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
			try:
				all_bookings=DBMS.getBookings('admin')
			except:
				all_bookings=None

		else:
			visitor=get_object_or_404(User, Id=request.session['visitor']['Id'])
			try:
				all_bookings=DBMS.getBookings('user', visitor)
			except:
				all_bookings=None

		return render(request, 'user/profile.html',{'visitor':visitor,'all_bookings':all_bookings,'err':err})
	except:
		request.session['err']='Not logged In...Please log in to continue'		
		return redirect('login')
    # return HttpResponse("User Hello world")


def search(request):
	cache.clear()
	# current_date=datetime.datetime.now().date()
	# raise Exception(current_date)
	current_date=datetime.datetime.now().date()

	try:
		checkIn=datetime.datetime.strptime(request.POST['checkIn'], "%Y-%m-%d").date()
		checkOut=datetime.datetime.strptime(request.POST['checkOut'], "%Y-%m-%d").date()


		if(checkIn< current_date or checkOut< current_date):
			request.session['err']=' cannot book past dates...'
			return redirect('user:dashboard')		
		if(checkIn> checkOut):
			request.session['err']=' CheckIn date must be before Checkout date...'
			return redirect('user:dashboard')
	except:
		pass
	visitor=get_object_or_404(User, Id=request.session['visitor']['Id'])
	try:
		if(request.POST['FoodId']):
			FoodId=request.POST['FoodId']
		else:
			FoodId=1
	except:
			FoodId=1



	try:
		if(request.POST['Reason'] != ""):
			obj=visitor.searchRoom(request.POST['checkIn'], request.POST['checkOut'], FoodId, request.POST['Reason'])
		else:
			raise Exception('Not a Waiting List Request')
 	except:
		obj=visitor.searchRoom(request.POST['checkIn'], request.POST['checkOut'], FoodId)

	try:
		if(isinstance(obj, Booking)):
			request.session['showBooking']=obj.GNR
			request.session['err']='Booking Successfull save GNR '+ str(obj.GNR) + ' for future refrence'
			return redirect('user:dashboard')
		# raise Exception('Not Entereing')
		# raise Exception(obj)
		
		request.session['showRooms']=obj
		request.session['request']=request.POST
		del obj
		return redirect('user:showRooms')
	except:
		del obj
		return redirect('user:showRooms')

	return HttpResponse(available_rooms)

def showBooking(request):
	# raise Exception(request.session['visitor']['Id'])
	try:																	
		if(request.POST['showBooking']):										# Check if the user wants to see his booking details
			request.session['showBooking']=request.POST['showBooking']
	except:
		pass

	try:
		if(request.session['showBooking']):
			booking=DBMS.getBookings('user', None, None, request.session['showBooking'])	# fetch corresponding booking
			# del request.session['showBooking']											## Uncomment this to redirect to dashboard on every refresh

			if(booking.UserId.Id==request.session['visitor']['Id']):						
				return render(request, 'user/showBookings.html',{'booking':booking})		# authenticated to view booking details
			else:
				raise Exception('User not authenticated to view booking')					# Not authenticated to view booking details
	except:
		request.session['err']='User not authenticated to view booking'
		return redirect('user:dashboard')
		


def showRooms(request):
	try:
		if(request.session['showRooms']):
			roomsList=request.session['showRooms']
			postedData=request.session['request']
			#del request.session['showRooms']												## Uncomment this to redirect to dashboard on every refresh
			return render(request, 'user/showRooms.html',{'roomsList':roomsList,'postedData':postedData})
	except:
		return redirect('user:dashboard')
		raise Exception(roomsList)

def cancel(request):
	# raise Exception(request.POST['GNR'])
	try:
		if(request.POST['GNR']):
			booking=DBMS.getBookings('user', None, None, request.POST['GNR'])	# fetch corresponding booking

	except:
		request.session['err']='INVALID BOOKING GNR'
		return redirect('user:dashboard')

	# try:
	visitor=get_object_or_404(User, Id=request.session['visitor']['Id'])
	visitor.cancelBooking(booking)
	request.session['err']='Booking Successfully cancelled'
	return redirect('user:dashboard')
	# except:
		# return redirect('user:dashboard')
