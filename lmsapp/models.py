 from __future__ import unicode_literals

from django.db import models


# Create your models here.
class LmsPost(models.Model):
	name =models.CharField(max_length=30)
	faculty =models.CharField(max_length=30)
	book =models.CharField(max_length=30)
	borrowed =models.DateTimeField(auto_now=False)
	duedate =models.DateTimeField(auto_now=False)
	returned =models.BooleanField(default=False)

	def __str__(self):
		return self.book


