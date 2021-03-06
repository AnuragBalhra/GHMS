from __future__ import unicode_literals
from datetime import datetime
from django.db import models

from basic.user.user import *
from basic.room import *
from basic.food import *
# Create your models here.


class Booking(models.Model):
	GNR = models.AutoField(primary_key=True)
	UserId = models.ForeignKey(User)
	RoomId = models.ForeignKey(Room)
	FoodId = models.ForeignKey(Food, default=1)
	StartTime = models.DateField()
	EndTime = models.DateField()
	AmountReq = models.CharField(max_length=100)
	AmountPaid = models.CharField(max_length=100)
	STATUS_CHOICES=(
		(1, "CNF"),
		(2, "WL"),
		(3, "CANCEL"),
		(4, "REJECTED"),
		(5, "CHECKED IN"),
		(6, "CHECKED OUT"),
		(0, "NIL")
		)
	Status =models.IntegerField(choices=STATUS_CHOICES, default=1) 
	Reason = models.CharField(max_length=1000,blank=True)

	BookingTime=models.DateTimeField(auto_now_add=True, blank=True)

	# def __init__(self, UserId, RoomId, FoodId, StartTime, EndTime, AmountReq, AmountPaid=0, Status=0, Reason=""):
	# 	self.UserId=UserId
	# 	self.RoomId=RoomId
	# 	self.FoodId=FoodId
	# 	self.StartTime=StartTime
	# 	self.EndTime=EndTime
	# 	self.AmountReq=AmountReq
	# 	self.AmountPaid=AmountPaid
	# 	self.Status=Status
	# 	self.Reason=Reason

	def __str__(self):
		return u'%s %s %s %s' %(str(self.GNR),str(self.UserId), str(self.RoomId), self.getStatus() )

	class Meta:
		ordering = ['GNR']

	def conflicting(self, StartTime, EndTime):
		# raise Exception(StartTime)
		if(StartTime<datetime.now().date() ):
			raise False
		if(self.EndTime<StartTime or self.StartTime>EndTime):
			return False
		return True

	def refund(self):
		if(self.getStatus()=='WL' or self.getStatus()=='CNF'):
			self.AmountPaid=0
			self.save()
			return 'Success'
		else:
			return 'Cannot Refund'

	def getStatus(self):
		STATUS_CHOICES=["NIL", "CNF","WL","CANCEL", "REJECTED", "CHECKED IN", "CHECKED IN", "UNDEFINED"]
		return STATUS_CHOICES[self.Status]

	def setStatus(self, Status):
		STATUS_CHOICES={"NIL":0, "CNF":1,"WL":2,"CANCEL":3, "REJECTED":4,"CHECKED IN":5, "CHECKED IN":6, "UNDEFINED":7}
		self.Status=STATUS_CHOICES[Status]
