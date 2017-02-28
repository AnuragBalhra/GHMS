from django.http import HttpResponseRedirect,HttpResponse  
import basic.person as bp
# import basic.guestHouse as bg
class User(bp.Person):

	
	def searchRoom(self, checkIn, checkOut, FoodId, Reason=""):
		import basic.guestHouse as bg
		if(Reason!=""):
			room=bg.GHMS.rooms[0]
			raise Exception('asdf')
			buking=self.requestBooking(room, checkIn, checkOut , FoodId, Reason)
			return buking

		roomsList=bg.GHMS.checkRoomsAvailability(checkIn, checkOut)
		# raise Exception(roomsList)

		if(isinstance(roomsList, dict) ):
			# raise Exception(roomsList)
			bg.GHMS.update()
			return roomsList
		else:
			# raise Exception(roomsList)
			# raise Exception("Hey")
			# cost=rum.cost
			# raise Exception(rum.Cost)
			buking=self.requestBooking(roomsList, checkIn, checkOut, FoodId)
			bg.GHMS.update()
			# raise Exception(buking)
			# del roomsList
			return buking


	def getProfileInfo(self):
		return self
	def requestBooking(self, rum, checkIn, checkOut, FoodId, Reason=""):
		import basic.guestHouse as bg
		import basic.dataBase as bd
		booking=bg.GHMS.bookRoom(self, rum, checkIn, checkOut, FoodId)
		if(Reason==""):
			booking.setStatus('CNF')
		else:
			booking.setStatus("WL")
			booking.Reason=Reason

		bd.DBMS.store(booking)
		return booking
	def makePayment(self, buking):
		import basic.guestHouse as bg
		return bg.GHMS.makePayment(self, buking.GNR)

	def requestRefund(self, buking):
		import basic.guestHouse as bg
		return bg.GHMS.makeRefund(self, buking.GNR)

