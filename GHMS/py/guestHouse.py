from room import room
from booking import booking
from dataBase import dataBase, DBMS

class guestHouse:

	def __init__(self):
		self.bookings=getBookings()
		self.rooms=getRooms()


	# def checkUser(self, email, pass):
	def bookRoom(self, usr, flat, checkIn, checkOut):
	def freeRoom(self, buking, usr, checkOutTime):
	def checkRoomsAvailability(self, checkIn, checkOut):
		delta=checkOut-checkIn
		roomsList=[len(rooms)][delta.days]
		for x in roomsList:
			for y in x:
				y=True
		buking=booking(checkIn, checkOut)
		allBookings=DBMS.getBookings()
		noConflict={}
		for x in rooms:
			noConflict[x.id]=True
			

		for var in allBookings:
			if(var.status=='CNF'):
				for x in range((var.startTime-checkIn).days,(var.endTime-checkIn).days):
					roomsList[var.rum.id][x]=False
				if(buking.conflicting(var)):
					noConflict[var.rum.id]=False

		cost=0
		for x in noConflict:
			if(noConflict[x]):
				rum=DBMS.getRooms(x)
				return rum
				

		return roomsList
	def checkBookingStatus(self, GNR):
	def makePayment(self, GNR):
	def makeRefund(self, GNR):
	def makeCancellation(self, GNR):


GHMS=guestHouse()