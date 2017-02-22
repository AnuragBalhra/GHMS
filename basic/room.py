from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class Room(models.Model):
	Id = models.AutoField(primary_key=True)
	Cost = models.CharField(max_length=40)
	TYPE_CHOICES=(
		(1, "Unreserved"),
		(2, "Reserved"),
		(3, "Not Available")
		)
	type =models.IntegerField(choices=TYPE_CHOICES, default=1)

	def __str__(self):
		return str(self.Id)

	class Meta:
		ordering = ['Id']

	# def __init__(self, cost):
	# 	self.cost=cost
	# 	self.status='Available'

	def gettype(self):
		TYPE_CHOICES=['NIL',"Unreserved","Reserved","Not Available"]
		return TYPE_CHOICES[self.type]

	def settype(self, type):
		TYPE_CHOICES={"Unreserved":1,"Reserved":2,"Not Available":3}
		self.type=TYPE_CHOICES[type]
