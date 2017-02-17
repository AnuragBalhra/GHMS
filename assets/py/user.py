from guestHouse import guestHouse, GHMS
from person import person
from booking import booking
from datetime import date

class user(person):
	def __init__(self):

	def searchRoom(self, checkIn, checkOut):
		delta=checkOut-checkIn
		roomsList=[len(GHMS.rooms)][delta.days]
		buking=booking(checkIn, checkOut)
		allBookings=getBookings()
		noConflict={}
		for x in GHMS.rooms:
			noConflict[x.id]=True
			

		for var in allBookings:
			if(var.status=='CNF'):
				if(buking.conflicting(var)):
					noConflict[var.rum.id]=False


		for x in noConflict:
			if(x):
				


		if(noConflict):
			buking.status='CNF'
			store(buking)
	def getProfileInfo(self):
	def requestBooking(self, usr, rum, checkIn, checkOut):
	def makePayment(self, buking):
	def requestRefund(self, buking):
