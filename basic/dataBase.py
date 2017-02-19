from django.shortcuts import get_object_or_404, render, redirect


from basic.user import *
from basic.admin import *
from basic.food import *
from basic.booking import *
from basic.guestHouse import *
# from basic.dataBase import *


class dataBase:
	def __init__(self):
		self.host=""
		self.username=""
		self.password=""

	def check(self, username, password, type):
		if type=='admin':
			admin=get_object_or_404(Administrator, Name=username)
			if(admin.Password==password):
				return True
			else:
				return False
		else:
			user=get_object_or_404(User, Name=username)
			if(user.Password==password):
				return True
			else:
				return False

	def checkBookings(self, rooms, checkIn, checkOut):
		return None

	def getBookings(self, type, usr=None, rum=None, GNR=0):
		if(type=='admin'):
			if(rum!=None):
				bukings=Booking.objects.filter(RoomId=rum.id)
				return bukings
			if(usr!=None):
				bukings=Booking.objects.filter(UserId=usr.id)
				return bukings
			if(GNR!=0):
				bukings=Booking.objects.filter(GNR=GNR)
				return bukings
			
			bukings=Booking.objects.all
			return bukings
		else:
			if(usr!=None):
				bukings=Booking.objects.filter(UserId=usr.Id)
				return bukings
			if(GNR!=0):
				bukings=Booking.objects.filter(GNR=GNR)
				return bukings
			
			bukings=Booking.objects.all
			return bukings


			

	def getUsers(self, id=0, name="", email=""):
		if(id!=0):
			users=get_object_or_404(User, id=id)
			return users
		elif(name!=""):
			users=get_object_or_404(User, name=name)
			return users
		elif(email!=""):
			users=get_object_or_404(User, email=email)
			return users
		
		users=User.objects.all
		return users
	def getRooms(self, roomNo=0):
		if(roomNo!=0):
			rooms=get_object_or_404(Room, id=roomNo)
			return rooms
		
		rooms=Room.objects.all
		return rooms

	def getFoods(self):
		foods=Food.objects.all
		return foods

	def store(self, obj):
		if(isinstance(obj, User)):
			obj2=User(obj)
			obj2.save()
			return obj2
		elif(isinstance(obj, Administrator)):
			obj2=Administrator(obj)
			obj2.save()
			return obj2
		elif(isinstance(obj, Room)):
			obj2=Room(obj)
			obj2.save()
			return obj2
		elif(isinstance(obj, Booking)):
			obj2=Booking(obj)
			obj2.save()
			return obj2
		elif(isinstance(obj, Food)):
			obj2=Food(obj)
			obj2.save()
			return obj2


	def deleteObj(seelf, obj):
		if(isinstance(obj, User)):
			User.objects.filter(id=obj.id).delete()
		elif(isinstance(obj, Administrator)):
			Administrator.objects.filter(id=obj.id).delete()
		elif(isinstance(obj, Room)):
			Room.objects.filter(id=obj.id).delete()
		elif(isinstance(obj, Booking)):
			Booking.objects.filter(GNR=obj.GNR).delete()
		elif(isinstance(obj, Food)):
			Food.objects.filter(id=obj.id).delete()


DBMS=dataBase()
