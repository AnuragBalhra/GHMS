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
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		try:
			all_bookings=DBMS.getBookings('admin')
			roomsList=DBMS.getRooms('admin')
			usersList=DBMS.getUsers()
		except:
			all_bookings=None
			roomsList=None
			usersList=None
	# raise Exception(usersList)
	return render(request, 'admin/profile.html',{'visitor':visitor,'all_bookings':all_bookings,'roomsList':roomsList, 'usersList':usersList})


def search(request):
	visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
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

	# try:
	if(isinstance(obj, Booking)):
		request.session['showBooking']=obj.GNR
		return redirect('administrator:showBooking')
	# raise Exception('Not Entereing')
	# raise Exception(obj)
	
	request.session['showRooms']=obj
	return redirect('administrator:showRooms')
	# except:
	# 	return redirect('administrator:showRooms')

	# return HttpResponse(available_rooms)

def showBooking(request):
	# raise Exception(request.session['visitor']['Id'])
	try:																	
		if(request.POST['showBooking']):										# Check if the user wants to see his booking details
			request.session['showBooking']=request.POST['showBooking']
	except:
		pass

	try:
		if(request.session['showBooking']):
			booking=DBMS.getBookings('admin', None, None, request.session['showBooking'])	# fetch corresponding booking
			del request.session['showBooking']

			if(booking.UserId.Id==request.session['visitor']['Id'] or request.session['visitor']['type']=='admin'):						
				return render(request, 'admin/showBookings.html',{'booking':booking})		# authenticated to view booking details
			else:
				raise Exception('User not authenticated to view booking')					# Not authenticated to view booking details
	except:
		request.session['err']='User not authenticated to view booking'
		return redirect('administrator:dashboard')
		



def showRoom(request):
	# raise Exception(request.session['visitor']['Id'])
	try:																	
		if(request.POST['showRoom']):										# Check if the user wants to see his booking details
			request.session['showRoom']=request.POST['showRoom']
	except:
		pass

	try:
		if(request.session['showRoom']):
			room=DBMS.getRooms('admin', request.session['showRoom'])	# fetch corresponding booking
			del request.session['showRoom']

			if( request.session['visitor']['type']=='admin'):						
				return render(request, 'admin/showRoom.html',{'room':room})		# authenticated to view booking details
			else:
				raise Exception('User not authenticated to view Room')					# Not authenticated to view booking details
	except:
		request.session['err']='User not authenticated to view Room'
		return redirect('administrator:dashboard')




def showUser(request):
	# raise Exception(request.POST['showUser'])
	try:																	
		if(request.POST['showUser']):										# Check if the user wants to see his booking details
			request.session['showUser']=request.POST['showUser']
	except:
		pass

	try:
		if(request.session['showUser']):
			user=DBMS.getUsers(request.session['showUser'])	# fetch corresponding booking
			del request.session['showUser']

			if( request.session['visitor']['type']=='admin'):						
				return render(request, 'admin/showUser.html',{'user':user})		# authenticated to view booking details
			else:
				raise Exception('User not authenticated to view user')					# Not authenticated to view booking details
	except:
		request.session['err']='User not authenticated to view user'
		return redirect('administrator:dashboard')





def showRooms(request):
	try:
		if(request.session['showRooms']):
			roomsList=request.session['showRooms']
			del request.session['showRooms']
			return render(request, 'admin/showRooms.html',{'roomsList':roomsList})
	except:
		return redirect('administrator:dashboard')
		raise Exception(roomsList)

def cancel(request):
	# raise Exception(request.POST['GNR'])
	try:
		if(request.POST['GNR']):
			# raise Exception(request.POST['GNR'])
			booking=DBMS.getBookings('admin', None, None, request.POST['GNR'])	# fetch corresponding booking

	except:
		request.session['err']='INVALID BOOKING GNR'
		return redirect('administrator:dashboard')

	try:
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		# raise Exception(visitor.Name)
		visitor.cancelBooking(booking)
		return redirect('administrator:dashboard')
	except:
		return redirect('administrator:dashboard')

def confirm(request):
	# raise Exception(request.POST['GNR'])
	try:
		if(request.POST['GNR']):
			# raise Exception(request.POST['GNR'])
			booking=DBMS.getBookings('admin', None, None, request.POST['GNR'])	# fetch corresponding booking

	except:
		request.session['err']='INVALID BOOKING GNR'
		return redirect('administrator:dashboard')

	# raise Exception(booking)

	try:
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		if(visitor.confirmBooking(booking) != 'Confirmed'):
			request.session['err']='Unknown Error'
			raise Exception('Unknown Error')
	except:
		return redirect('administrator:dashboard')
	
	return redirect('administrator:dashboard')


def delUser(request):
	try:
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		if(visitor.deleteUser(request.POST['UserId']) != 'Success'):
			request.session['err']='Unknown Error'
			raise Exception('Unknown Error')
	except:
		return redirect('administrator:dashboard')
	
	return redirect('administrator:dashboard')

def delRoom(request):
	# raise Exception(request.POST['RoomId'])
	try:
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		if(visitor.deleteRoom(request.POST['RoomId']) == 0):
			request.session['err']='Unknown Error'
			raise Exception('Unknown Error')
	except:
		return redirect('administrator:dashboard')
	
	return redirect('administrator:dashboard')



def addObj(request):
	# raise Exception(request.POST['type'])
	try:
		if(request.POST['typeOfObj']!="room" and request.POST['typeOfObj']!="user"):
			request.session['err']='Unknown Object'
			raise Exception('Unknown Object')
	except:
		return redirect('administrator:dashboard')

	try:
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['Id'])
		if(request.POST['typeOfObj']=='user'):
			visitor.addUser(request)

		elif(request.POST['typeOfObj']=='room'):
			visitor.addRoom(request)
		
		# request.session['err']='Unknown Error'
		raise Exception('Unknown Error')
	except:
		return redirect('administrator:dashboard')
	
	return redirect('administrator:dashboard')
