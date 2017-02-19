from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class Food(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=40)
	Status = models.CharField(max_length=10)

	def __str__(self):
		return self.Name

	class Meta:
		ordering = ['Id']
