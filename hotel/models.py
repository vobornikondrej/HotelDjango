from __future__ import unicode_literals

from django.db import models

class Hotels(models.Model):
	name = models.CharField(max_length=50)
	destination = models.CharField(max_length=100, default="")
	number_of_rooms = models.IntegerField(default=0)
	price_per_night = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name


		