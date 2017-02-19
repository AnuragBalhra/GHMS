from dataBase import dataBase
from booking import booking
from guestHouse import guestHouse

class person:

	def __init__(self, name, password, email):
		self.name=name
		self.password=password
		self.email=email

	def login(self, email, password):
		return(check(email, password)) 

	def cancelBooking(self, buking):
		return(makeCancellation(buking.GNR)) 

