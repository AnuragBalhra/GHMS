from basic.person import *
class User(Person):
	def login(self, email, password):
		return(check(email, password)) 

	def cancelBooking(self, buking):
		return(makeCancellation(buking.GNR)) 

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

