from dataBase import dataBase
from booking import booking
from guestHouse import guestHouse

class person:

	def __init__(self):
		self.name=""
		self.id=""
		self.password=""
		self.email=""

	def login(self, email, pass):
		return(check(email, pass)) 

	def cancelBooking(self, buking):
		return(makeCancellation(buking.GNR)) 

