from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.sessions.backends.db import SessionStore



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

	def login(self, username, password, type):
		import basic.dataBase as DB
		return(DB.DBMS.check(username,password, type))

	def cancelBooking(self, buking):
		import basic.guestHouse as bg
		try:
			if(buking.UserId.Id != self.Id and self.type != 'admin'):
				raise Exception(' User Not Authenticateed to Cancel The Ticket ')
		except:
			request.session['err']=' User Not Authenticateed to Cancel The Ticket '
			return 'FAIL'
		return(bg.GHMS.makeCancellation(buking.GNR)) 

		# return(check(email, password)) 

