from django.db import models
from datetime import datetime

class User(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=30)
	Password = models.CharField(max_length=50)
	Email = models.EmailField(blank=True)

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Id']

class Admin(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=30)
	Password = models.CharField(max_length=50)
	Email = models.EmailField()

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Id']

class Room(models.Model):
	Id = models.AutoField(primary_key=True)
	Cost = models.CharField(max_length=40)
	Status = models.CharField(max_length=10)

	def __str__(self):
		return str(self.Id)

	class Meta:
		ordering = ['Id']


class Food(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=40)
	Status = models.CharField(max_length=10)

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Id']


class Booking(models.Model):
	GNR = models.AutoField(primary_key=True)
	UserId = models.ForeignKey(User)
	RoomId = models.ForeignKey(Room)
	FoodId = models.ForeignKey(Food, default=1.)
	StartTime = models.DateField()
	EndTime = models.DateField()
	AmountReq = models.CharField(max_length=100)
	AmountPaid = models.CharField(max_length=100)
	STATUS_CHOICES=(
		(1, "CNF"),
		(2, "WL"),
		(3, "CANCEL"),
		(4, "REJECTED"),
		(0, "NIL")
		)
	Status =models.IntegerField(choices=STATUS_CHOICES, default=1) 
	Reason = models.CharField(max_length=1000,blank=True)

	BookingTime=models.DateTimeField(auto_now_add=True, blank=True)


	def __str__(self):
		return u'%s %s %s' %(str(self.GNR),str(self.UserId), str(self.RoomId)) 

	class Meta:
		ordering = ['GNR']
