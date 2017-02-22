import basic.person as bp
class Administrator(bp.Person):
	def addUser(self, request):
		if(request.POST['type']=='user'):
			import basic.user.user as bu
			user=bu.User.objects.create(Name=request.POST['Name'], Password=request.POST['Password'], Email=request.POST['Email'], type=request.POST['type'])
			raise Exception(user.Id)
			return user
		elif(request.POST['type']=='admin'):
			admin=Administrator.objects.create(Name=request.POST['Name'], Password=request.POST['Password'], Email=request.POST['Email'], type=request.POST['type'])
			raise Exception(admin.Id)
			return admin

	def deleteUser(self, UserId):
		import basic.dataBase as bd
		user=bp.Person.objects.get(Id=UserId)
		result=bd.DBMS.deleteObj(user)
		return result
	def addRoom(self, request):
		import basic.room as br
		room=br.Room.objects.create(Cost=request.POST['Cost'], type=request.POST['type'])
		# raise Exception(room)

		# rum=DBMS.store(rum)
		return room
	def deleteRoom(self, RoomId):
		import basic.dataBase as bd
		import basic.room as br
		room=br.Room.objects.get(Id=RoomId)
		result=bd.DBMS.deleteObj(room)
		raise Exception(result)
		return result
	def rejectBooking(self):
		import basic.guestHouse as bg
		import basic.dataBase as bd

		try:
			if(request.POST['GNR']):
				booking=db.DBMS.getBookings('admin', None, None, request.POST['GNR'])	# fetch corresponding booking

		except:
			request.session['err']='INVALID BOOKING GNR'
			return redirect('administrator:dashboard')

		bg.GHMS.makeRefund(GNR)

		if(booking.getStatus()=='WL' or booking.getStatus()=='CNF'):
			booking.setStatus('REJECTED')
			booking.save()
			return 'Success'
		return 'Cannot Cancel'



	def confirmBooking(self, booking):
		import basic.guestHouse as bg
		import basic.dataBase as bd
		import basic.booking as bb
		import basic.room as br

		

		allBookings=bb.Booking.objects.filter(Status=2)
		rooms=br.Room.objects.filter(type=2)
		noConflict={}
		for x in rooms:
			noConflict[x.Id]=True

		for var in allBookings:
			if(var.getStatus=='CNF'):
				if(var.conflicting(booking.StartTime, booking.EndTime)):
					noConflict[var.RoomId.Id-1]=False
		for x in noConflict:
			if(noConflict[x]):
				# raise Exception(x)									#raise exception to print roomList
				booking.RoomId=bd.DBMS.getRooms('admin',x)
				# raise Exception(bd.DBMS.getRooms('admin',x))
				booking.setStatus('CNF')
				# raise Exception(x+1)
				if(bd.DBMS.store(booking)=='Success'):
					return 'Confirmed'
		raise Exception('Cannot Confirm Booking')


	def checkIn(self, GNR, UserId):
		import basic.dataBase as bd
		booking=bd.DBMS.getBookings('admin', None, None, GNR )
		try:
			if(booking.UserId.Id==UserId):
				booking.setStatus('CHECKED IN')
				bd.DBMS.store(booking)
				return True
			else:
				err=' User does not have permission to CheckIn on given booking '
				raise Exception(err)
		except:
			request.session['err']=err
			return False

		
		
	def checkOut(self, buking, usr):
		import basic.dataBase as bd
		booking=bd.DBMS.getBookings('admin', None, None, GNR )
		try:
			if(booking.UserId.Id==UserId):
				if(booking.getStatus()!='CHECKED IN'):
					err='Nobody has checked in to given booking yet... Unable to checkout'
					raise Exception(err)
				booking.setStatus('CHECKED OUT')
				bd.DBMS.store(booking)
				return True
			else:
				err=' User does not have permission to CheckIn on given booking '
				raise Exception(err)
		except:
			request.session['err']=err
			return False


