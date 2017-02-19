from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class Room(models.Model):
	Id = models.AutoField(primary_key=True)
	Cost = models.CharField(max_length=40)
	TYPE_CHOICES=(
		(1, "Unreserved"),
		(2, "reserved"),
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

	def checkStatus(self):
		return self.status

	def changeStatus(self):
		if(self.status=='Available'):
			self.status='Not Available'
		else:
			self.status=='Available'	