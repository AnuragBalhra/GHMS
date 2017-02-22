from django.shortcuts import get_object_or_404, render, redirect


import basic.user.user as bu
import basic.administrator.administrator as ba
import basic.food as bf
import basic.booking as bb
from basic.guestHouse import *
# import basic.guestHouse as bg
# from basic.dataBase import *


class dataBase:
	def __init__(self):
		self.host=""
		self.username=""
		self.password=""

	def check(self, username, password, type):
		if type=='admin':
			admin=get_object_or_404(ba.Administrator, Name=username)
			if(admin.Password==password):
				return True
			else:
				return False
		else:
			user=get_object_or_404(bu.User, Name=username)
			if(user.Password==password):
				return True
			else:
				return False

	def checkBookings(self, rooms, checkIn, checkOut):
		return None

	def getBookings(self, type, usr=None, rum=None, GNR=0):
		if(type=='admin'):
			if(rum!=None):
				bookings=bb.Booking.objects.filter(RoomId=rum.id)
				return bookings
			if(usr!=None):
				bookings=bb.Booking.objects.filter(UserId=usr.id)
				return bookings
			if(GNR!=0):
				bookings=bb.Booking.objects.get(GNR=GNR)
				return bookings
			
		else:
			if(usr!=None):
				bookings=bb.Booking.objects.filter(UserId=usr.Id)
				return bookings
			if(GNR!=0):
				bookings=bb.Booking.objects.get(GNR=GNR)
				return bookings
			
		bookings=bb.Booking.objects.all()
		return bookings


			

	def getUsers(self, Id=0, name="", email=""):
		if(Id!=0):
			users=get_object_or_404(bu.User, Id=Id)
			return users
		elif(name!=""):
			users=bu.User.objects.filter(name=name)
			return users
		elif(email!=""):
			users=bu.User.objects.filter(email=email)
			return users
		
		users=bu.User.objects.all()
		return users
	def getRooms(self, type, roomNo=0):
		if(roomNo!=0):
			# raise Exception(roomNo)
			rooms=get_object_or_404(br.Room, Id=roomNo)
			# raise Exception(rooms.Cost)
			return rooms
		try:
			if(type=='admin'):
				rooms=br.Room.objects.all()
			elif(type=='user'):
				rooms=br.Room.objects.filter(type=1)
			else:
				err='Unknown User querying rooms'				
				raise Exception(err)
		except:
			return None
		return rooms

	def getFoods(self):
		foods=bf.Food.objects.all()
		return foods

	def store(self, obj):
		try:
			obj.save()
			return "Success"
		except:
			return "Fail"

		# if(isinstance(obj, bu.User)):
		# 	obj2=bu.User(obj)
		# 	obj2.save()
		# 	return obj2
		# elif(isinstance(obj, ba.Administrator)):
		# 	obj2=ba.Administrator(obj)
		# 	obj2.save()
		# 	return obj2
		# elif(isinstance(obj, br.Room)):
		# 	obj2=br.Room(obj)
		# 	obj2.save()
		# 	return obj2
		# elif(isinstance(obj, bb.Booking)):
		# 	# raise Exception(obj)
		# 	# obj2=bb.Booking(obj)
		# 	obj.save()
		# 	return obj
		# elif(isinstance(obj, bf.Food)):
		# 	obj2=bf.Food(obj)
		# 	obj2.save()
		# 	return obj2


	def deleteObj(self, obj):
		try:
			obj.delete()
			return 'Success'
		except:
			return 'Fail'
		# try:
		# 	if(isinstance(obj, bu.User)):
		# 		bu.User.objects.filter(id=obj.id).delete()
		# 	elif(isinstance(obj, ba.Administrator)):
		# 		ba.Administrator.objects.filter(id=obj.id).delete()
		# 	elif(isinstance(obj, br.Room)):
		# 		br.Room.objects.filter(id=obj.id).delete()
		# 	elif(isinstance(obj, bb.Booking)):
		# 		bb.Booking.objects.filter(GNR=obj.GNR).delete()
		# 	elif(isinstance(obj, bf.Food)):
		# 		bf.Food.objects.filter(id=obj.id).delete()
		# 	return "Success"
		# except:
		# 	return "Fail"


DBMS=dataBase()
