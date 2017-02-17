from person import person
from user import user
from dataBase import dataBase
from booking import booking
from guestHouse import guestHouse
from room import room
from food import food

class admin(person):

	def __init__(self):

	def addUser(self, usr):
		usr=store(usr)
		return usr

	def deleteUser(self, usr):
		result=deleteObj(usr)
		return result
	def addRoom(self, rum):
		rum=store(rum)
		return rum
	def deleteRoom(self, rum):
		result=deleteObj(rum)
		return result
	def confirmBooking(self, buking):
		buking=getBookings(buking.GNR)
		allBookings=getBookings()
		noConflict=True
		for var in allBookings:
			if(var.status=='CNF'):
				if(buking.conflicting(var)):
					noConflict=False
					break
		if(noConflict):
			buking.status='CNF'
			store(buking)

	def checkIn(self, buking, usr):
		buking=getBookings(buking.GNR)
		buking.status='CheckedIn'
		store(buking)
		
		
	def checkOut(self, buking, usr):

		buking=getBookings(buking.GNR)
		buking.status='CheckedOut'
		store(buking)