from django.http import HttpResponseRedirect,HttpResponse  
import basic.person as bp
# import basic.guestHouse as bg
class User(bp.Person):

	def cancelBooking(self, buking):
		return(makeCancellation(buking.GNR)) 

	def searchRoom(self, checkIn, checkOut):
		import basic.guestHouse as bg
		roomsList=bg.GHMS.checkRoomsAvailability(checkIn, checkOut)
		# return HttpResponse(rum[0].Cost)

		try:
			if(len(roomsList)>1):
				return roomsList

		except:
			# cost=rum.cost
			# raise Exception(rum.Cost)

			buking=bg.GHMS.bookRoom(self, roomsList, checkIn, checkOut)
			return buking


	def getProfileInfo(self):
		return self.name
	def requestBooking(self, rum, checkIn, checkOut):
		buking=GHMS.bookRoom(self, rum, checkIn, checkOut)
		buking.status="WL"
		DBMS.store(buking)
	def makePayment(self, buking):
		import basic.guestHouse as bg
		return bg.GHMS.makePayment(self, buking)

	def requestRefund(self, buking):
		return None

