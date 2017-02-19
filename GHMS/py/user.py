from guestHouse import guestHouse, GHMS
from person import person
from booking import booking
from dataBase import dataBase, DBMS
from datetime import date

class user(person):
	def __init__(self):
		self.id=0

	def searchRoom(self, checkIn, checkOut):
		rum=GHMS.checkRoomsAvailability(checkIn, checkOut)
		try:
			if(len(rum)>1):
				return rum

		except:
			cost=rum.cost
			buking=GHMS.bookRoom(self, rum, checkIn, checkOut)
			return buking.status


	def getProfileInfo(self):
		return self.name
	def requestBooking(self, rum, checkIn, checkOut):
		buking=GHMS.bookRoom(self, rum, checkIn, checkOut)
		buking.status="WL"
		DBMS.store(buking)
	def makePayment(self, buking):
		return None
	def requestRefund(self, buking):
		return None
