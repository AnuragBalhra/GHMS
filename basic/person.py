from __future__ import unicode_literals
from datetime import datetime
from django.db import models




class Person(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=30)
	Password = models.CharField(max_length=50)
	Email = models.EmailField(blank=True)
	type =models.CharField(max_length=30)

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Id']

