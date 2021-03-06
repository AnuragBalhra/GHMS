from django.http import HttpResponseRedirect,HttpResponse  
import basic.room as br
import basic.booking as bb
import basic.dataBase as bd
import datetime
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import get_object_or_404, render, redirect


class guestHouse:

	def __init__(self):
		self.bookings=bd.DBMS.getBookings('user')
		# return None
		self.rooms=bd.DBMS.getRooms('user')
		# raise Exception(self.bookings)
	def update(self):
		self.bookings=bd.DBMS.getBookings('user')
		self.rooms=bd.DBMS.getRooms('user')
		# raise Exception(self.bookings)
	# def checkUser(self, email, pass):
	def bookRoom(self, usr, flat, checkIn, checkOut, FoodId, reason=""):
		# raise Exception(usr)
		import basic.food as bf
		food=bf.Food.objects.get(Id=FoodId)

		new_booking=bb.Booking.objects.create(UserId=usr,RoomId=flat, FoodId=food, StartTime=checkIn, EndTime=checkOut, AmountReq=flat.Cost, Status=0)
		status=self.makePayment(new_booking.GNR)
		# new_booking=bb.Booking()
		# new_booking.UserId=usr
		# new_booking.RoomId=flat
		if(status!='Success'):
			deleted=bd.DBMS.deleteObj(new_booking)
			if(deleted!='Success'):
				raise Exception("Unable to Delete booking")
			raise Exception("Payment Failed...")
		else:
			new_booking.AmountPaid=flat.Cost
		# new_booking.save()
		return new_booking
	def freeRoom(self, buking, usr, checkOutTime):
		pass
	def checkRoomsAvailability(self, checkIn, checkOut):
		# raise Exception(self.rooms)

		checkIn=datetime.datetime.strptime(checkIn, "%Y-%m-%d").date()
		checkOut=datetime.datetime.strptime(checkOut, "%Y-%m-%d").date()
		
		delta=(checkOut-checkIn+ datetime.timedelta(days=1)).days
		# raise Exception(delta)

		if(delta<=0):
			raise Exception(str(delta)+" cannot be negative. Invalid Dates selected")
		# return HttpResponse(self.bookings[0].UserId.Id)

		# roomsList={}

		# for r in self.rooms:
		# 	temp={}
		# 	for x in range(delta.days):
		# 		temp.update({x:True})
		# 	roomsList.update({r.Id: temp})
		roomsList={y.Id:{str(checkIn+datetime.timedelta(x)):True for x in range(delta)} for y in self.rooms}
		# buking=bb.Booking(checkIn, checkOut)
		allBookings=self.bookings
		noConflict={}
		for y in self.rooms:
			noConflict[y.Id]=True

			
		# test={}
		for var in allBookings:
			if(var.Status==1 and var.RoomId.type==1):

				for x in range(delta):
					temp_date=checkIn+datetime.timedelta(x)
					# roomsList[var.RoomId.Id][temp_date.day]=False
					# raise Exception(roomsList)
					if(temp_date>=var.StartTime and temp_date<=var.EndTime):
						# test[temp_date.day]=var.RoomId.Id
						roomsList[var.RoomId.Id][str(temp_date)]=False


				if(var.conflicting(checkIn, checkOut)):
					noConflict[var.RoomId.Id]=False
		# for x in roomsList:
		# raise Exception(noConflict)

		for x in noConflict:
			if(noConflict[x]):
				# raise Exception(x)									#raise exception to print roomList

				rum=bd.DBMS.getRooms('user',x)
				return rum
				
		# raise Exception(roomsList)

		return roomsList
	def checkBookingStatus(self, GNR):
		booking=bd.DBMS.getBookings('user', None, None, GNR)
		return booking.getStatus()
	def makePayment(self, GNR):
		booking=bd.DBMS.getBookings('user', None, None, GNR)
		if(booking.getStatus()=='WL'):
			return 'Payment Already Done'
		else:
			booking.AmountPaid=booking.AmountReq
		return "Success"
	def makeRefund(self, GNR):
		# import pdb
		# pdb.set_trace()
		booking=bd.DBMS.getBookings('user', None, None, GNR)
		Status=booking.refund()
		if(Status=='Success'):
			booking.AmountPaid=0
			booking.save()
			return 'Success'
		else:
			return Status




	def makeCancellation(self, GNR):
		self.makeRefund(GNR)

		booking=bd.DBMS.getBookings('user', None, None, GNR)
		if(booking.getStatus()=='WL' or booking.getStatus()=='CNF'):
			booking.setStatus('CANCEL')
			bd.DBMS.store(booking)
			# raise Exception(datetime.datetime.now().date())
			# from basic.dataBase import DBMS
			from basic.admin import Administrator
			
			try:
				bookings=bb.Booking.objects.filter(StartTime__gte = datetime.datetime.now().date())

				# bookings=bd.DBMS.getBookings('admin')	# fetch corresponding booking

			except:
				pass
			# raise Exception(bookings)

			try:
				visitor=get_object_or_404(Administrator, Id=1)
				for buking in bookings:
					if(buking.getStatus()=='WL'):
						visitor.confirmBooking(buking)
						# raise Exception(buking.GNR) 
			except:
				pass
			# raise Exception(buking.GNR) 
			return 'Success'

		elif(booking.getStatus()=='CANCEL'):
			return 'Already Cancelled'
		return 'Cannot Cancel'


GHMS=guestHouse()