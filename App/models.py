from django.db import models
from django.contrib.auth.models import *


class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True)
	unique_id = models.CharField(max_length=8, default='00000000') #Must set defaults or nullables for migratiions
	
	def __unicode__(self):
		return self.user or u'' #returns a blank string if no user can be found
	
class ProjectProfile(models.Model):
	pname = models.CharField(max_length=32, primary_key = True)
	ppassword = models.CharField(max_length=100)
	pabout = models.CharField(max_length=160)
	user = models.ManyToManyField(User, null=True) 
	
	def __unicode__(self):
		return self.pname or u''
		
class AddTask(models.Model):
	user =  models.ForeignKey(User, null=False)
	date = models.CharField(max_length=11)
	descr = models.CharField(max_length = 160)
	
	def __unicode__(self):
		return self.date or u''
		
class Match(models.Model):
	userID = models.ForeignKey(UserProfile)
	projectID = models.ForeignKey(ProjectProfile)
	
