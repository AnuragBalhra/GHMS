from person import person
from user import user
from dataBase import dataBase, DBMS
from booking import booking
from guestHouse import guestHouse
from room import room
from food import food

class admin(person):

	def __init__(self):

	def addUser(self, usr):
		usr=DBMS.store(usr)
		return usr

	def deleteUser(self, usr):
		result=DBMS.deleteObj(usr)
		return result
	def addRoom(self, rum):
		rum=DBMS.store(rum)
		return rum
	def deleteRoom(self, rum):
		result=DBMS.deleteObj(rum)
		return result
	def confirmBooking(self, buking):
		buking=DBMS.getBookings(buking.GNR)
		allBookings=DBMS.getBookings('admin')
		noConflict=True
		for var in allBookings:
			if(var.status=='CNF'):
				if(buking.conflicting(var)):
					noConflict=False
					break
		if(noConflict):
			buking.status='CNF'
			DBMS.store(buking)

	def checkIn(self, buking, usr):
		buking=DBMS.getBookings(buking.GNR, 'admin')
		buking.status='CheckedIn'
		DBMS.store(buking)
		
		
	def checkOut(self, buking, usr):

		buking=DBMS.getBookings(buking.GNR, 'admin')
		buking.status='CheckedOut'
		DBMS.store(buking)