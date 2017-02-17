from room import room
from booking import booking
from dataBase import dataBase

class guestHouse:

	def __init__(self):
		self.bookings=getBookings()
		self.rooms=getRooms()


	def checkUser(self, email, pass):
	def bookRoom(self, usr, flat, checkIn, checkOut):
	def freeRoom(self, buking, usr, checkOutTime):
	def checkRoomsAvailability(self, checkIn, checkOut):
	def checkBookingStatus(self, GNR):
	def makePayment(self, GNR):
	def makeRefund(self, GNR):
	def makeCancellation(self, GNR):


GHMS=guestHouse()