from django.http import HttpResponseRedirect,HttpResponse  
import basic.room as br
import basic.booking as bb
import basic.dataBase as bd
from datetime import datetime


class guestHouse:

	def __init__(self):
		self.bookings=bd.DBMS.getBookings('user')
		# return None
		self.rooms=bd.DBMS.getRooms()
		# raise Exception(self.bookings)


	# def checkUser(self, email, pass):
	def bookRoom(self, usr, flat, checkIn, checkOut, reason=""):
		# raise Exception(usr)
		import basic.food as bf
		food=bf.Food.objects.get(Id=1)

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
		# new_booking.save()
		return new_booking
	def freeRoom(self, buking, usr, checkOutTime):
		pass
	def checkRoomsAvailability(self, checkIn, checkOut):
		# raise Exception(self.rooms)

		checkIn=datetime.strptime(checkIn, "%Y-%m-%d")
		checkOut=datetime.strptime(checkOut, "%Y-%m-%d")
		delta=checkOut-checkIn
		# return HttpResponse(self.bookings[0].UserId.Id)

		# roomsList={}

		# for r in self.rooms:
		# 	temp={}
		# 	for x in range(delta.days):
		# 		temp.update({x:True})
		# 	roomsList.update({r.Id: temp})
		roomsList=[[True for x in range(delta.days)] for y in range(len(self.rooms))]
		# buking=bb.Booking(checkIn, checkOut)
		allBookings=self.bookings
		noConflict={}
		for x in self.rooms:
			noConflict[x.Id-1]=True
			
		# raise Exception(buking)
		# temp=""

		for var in allBookings:
			# temp+=str(var.Status)
			if(var.Status==1):
				# for x in range((var.StartTime-checkIn).days,(var.endTime-checkIn).days):
				begin_loop=(var.StartTime-checkIn.date()).days
				if(begin_loop<0):
					begin_loop=0
				if(begin_loop>delta.days):
					begin_loop=delta.days
				end_loop=(var.EndTime-checkIn.date()).days
				if(end_loop<0):
					end_loop=0
				if(end_loop>delta.days):
					end_loop=delta.days

				# raise Exception(end_loop)
				# temp+=str(diff)
				for x in range(begin_loop, end_loop ):
					roomsList[var.RoomId.Id-1][x]=False
				if(var.conflicting(checkIn.date(), checkOut.date())):
					noConflict[var.RoomId.Id-1]=False
		# raise Exception(noConflict)									#raise exception to print roomList

		cost=0
		for x in noConflict:
			if(noConflict[x]):
				# raise Exception(x)									#raise exception to print roomList

				rum=bd.DBMS.getRooms(x+1)
				return rum
				

		return roomsList
	def checkBookingStatus(self, GNR):
		pass
	def makePayment(self, GNR):
		booking=bd.DBMS.getBookings('user', None, None, GNR)
		booking[0].AmountPaid=booking[0].AmountReq
		return "Success"
	def makeRefund(self, GNR):
		pass
	def makeCancellation(self, GNR):
		pass


GHMS=guestHouse()