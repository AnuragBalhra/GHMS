import basic.person as bp
# import basic.guestHouse as bg
class User(bp.Person):

	def cancelBooking(self, buking):
		return(makeCancellation(buking.GNR)) 

	def searchRoom(self, checkIn, checkOut):
		import basic.guestHouse as bg
		rum=bg.GHMS.checkRoomsAvailability(checkIn, checkOut)
		try:
			if(len(rum)>1):
				return rum

		except:
			cost=rum.cost
			buking=bg.GHMS.bookRoom(self, rum, checkIn, checkOut)
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

